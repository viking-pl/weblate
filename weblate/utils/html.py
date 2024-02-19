# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import re
from collections import defaultdict

import nh3
from html2text import HTML2Text as _HTML2Text
from lxml.etree import HTMLParser

MD_LINK = re.compile(
    r"""
    (?:
    !?                                                          # Exclamation for images
    \[((?:\[[^^\]]*\]|[^\[\]]|\](?=[^\[]*\]))*)\]               # Link text
    \(
        \s*(<)?([\s\S]*?)(?(2)>)                                # URL
        (?:\s+['"]([\s\S]*?)['"])?\s*                           # Title
    \)
    |
    <(https?://[^>]+)>                                          # URL
    |
    <([^>]+@[^>]+\.[^>]+)>                                      # E-mail
    )
    """,
    re.VERBOSE,
)
MD_BROKEN_LINK = re.compile(r"\] +\(")
MD_REFLINK = re.compile(
    r"!?\[("  # leading [
    r"(?:\[[^^\]]*\]|[^\[\]]|\](?=[^\[]*\]))*"  # link text
    r")\]\s*\[([^^\]]*)\]"  # trailing ] with optional target
)
MD_SYNTAX = re.compile(
    r"""
    (_{2})(?:[\s\S]+?)_{2}(?!_)         # __word__
    |
    (\*{2})(?:[\s\S]+?)\*{2}(?!\*)      # **word**
    |
    \b(_)(?:(?:__|[^_])+?)_\b           # _word_
    |
    (\*)(?:(?:\*\*|[^\*])+?)\*(?!\*)    # *word*
    |
    (`+)\s*(?:[\s\S]*?[^`])\s*\5(?!`)   # `code`
    |
    (~~)(?=\S)(?:[\s\S]*?\S)~~          # ~~word~~
    |
    (<)(?:https?://[^>]+)>              # URL
    |
    (<)(?:[^>]+@[^>]+\.[^>]+)>          # E-mail
    """,
    re.VERBOSE,
)
MD_SYNTAX_GROUPS = 8

IGNORE = {"body", "html"}

# Allow some chars:
# - non breakable space
SANE_CHARS = re.compile("[\xa0]")


class MarkupExtractor:
    def __init__(self):
        self.found_tags = set()
        self.found_attributes = defaultdict(set)

    def start(self, tag, attrs):
        if tag in IGNORE:
            return
        self.found_tags.add(tag)
        self.found_attributes[tag].update(attrs.keys())


def extract_html_tags(text):
    """Extract tags from text in a form suitable for HTML sanitization."""
    extractor = MarkupExtractor()
    parser = HTMLParser(collect_ids=False, target=extractor)
    parser.feed(text)
    return {"tags": extractor.found_tags, "attributes": extractor.found_attributes}


class HTMLSanitizer:
    def __init__(self):
        self.current = 0
        self.replacements = {}

    def clean(self, text: str, source: str, flags) -> str:
        self.current = 0
        self.replacements = {}

        text = self.remove_special(text, flags)

        source_tags = extract_html_tags(source)

        text = nh3.clean(text, link_rel=None, **source_tags)

        return self.add_back_special(text)

    def handle_replace(self, match):
        self.current += 1
        replacement = f"@@@@@weblate:{self.current}@@@@@"
        self.replacements[replacement] = match.group(0)
        return replacement

    def remove_special(self, text: str, flags) -> str:
        if "md-text" in flags:
            text = MD_LINK.sub(self.handle_replace, text)

        return SANE_CHARS.sub(self.handle_replace, text)

    def add_back_special(self, text: str) -> str:
        for replacement, original in self.replacements.items():
            text = text.replace(replacement, original)
        return text


# Map tags to open and closing text
WEBLATE_TAGS = {
    # Word diff syntax for text changes
    "ins": ("{+", "+}"),
    "del": ("[-", "-]"),
}


class HTML2Text(_HTML2Text):
    def __init__(self, bodywidth: int = 78):
        super().__init__(bodywidth=bodywidth)
        # Use Unicode characters instead of their ascii pseudo-replacements
        self.unicode_snob = True
        #  Do not include any formatting for images
        self.ignore_images = True
        # Pad the cells to equal column width in tables
        self.pad_tables = True
        # Hook additional callback for tags
        # This needs unbound method as it receives self as explicit arg
        self.tag_callback = self.__class__.handle_weblate_tags

    def handle_weblate_tags(
        self, tag: str, attrs: dict[str, str | None], start: bool
    ) -> bool:
        if tag in WEBLATE_TAGS:
            self.o(WEBLATE_TAGS[tag][not start])
            return True
        return False
