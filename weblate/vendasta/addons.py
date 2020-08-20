# -*- coding: utf-8 -*-
import os

import requests

from weblate.addons.base import BaseAddon
from weblate.addons.events import EVENT_POST_COMMIT
from weblate.logger import LOGGER
from weblate.utils.requests import request


class NotifyLexicon(BaseAddon):
    """Triggers on commit."""

    events = (EVENT_POST_COMMIT,)
    name = "weblate.vendasta.notifylexicon"
    verbose = "Notify Lexicon"
    description = "When this component commits changes, notify Lexicon"
    lexicon_url_template = (
        "https://lexicon-{env}.apigateway.co"
        "?componentName={component_name}&languageCode={language_code}"
    )

    def post_commit(self, component, translation=None):
        """Notify Lexicon after committing changes."""
        env = os.environ.get("ENVIRONMENT", "prod")
        component_name = "{}/{}".format(component.project.slug, component.slug)
        url = self.lexicon_url_template.format(
            env=env,
            component_name=component_name,
            language_code=translation.language_code,
        )
        response = request(
            "get",
            url,
            headers={
                "Authorization": "Token {}".format(
                    os.environ.get("WEBLATE_ADMIN_API_TOKEN")
                )
            },
        )
        if response.status_code != requests.codes.ok:
            LOGGER.error(
                "Unable to notify lexicon of changes to (%s, %s)",
                component.name,
                translation.language_code,
            )
