# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2018 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

############################################################################
# This is automatically generated file, see scripts/generate-language-data #
############################################################################
# pylint: disable=line-too-long,too-many-lines

from __future__ import unicode_literals
from django.utils.translation import ugettext_noop as _

# Language definitions
LANGUAGES = (
    (
        'aa',
        _('Afar'),
        2,
        'n != 1',
    ),
    (
        'ab',
        _('Abkhazian'),
        2,
        'n != 1',
    ),
    (
        'ace',
        _('Acehnese'),
        1,
        '0',
    ),
    (
        'ach',
        _('Acholi'),
        2,
        'n > 1',
    ),
    (
        'ady',
        _('Adyghe'),
        2,
        'n > 1',
    ),
    (
        'ae',
        _('Avestan'),
        2,
        'n != 1',
    ),
    (
        'af',
        _('Afrikaans'),
        2,
        'n != 1',
    ),
    (
        'ak',
        _('Akan'),
        2,
        'n > 1',
    ),
    (
        'am',
        _('Amharic'),
        2,
        'n > 1',
    ),
    (
        'an',
        _('Aragonese'),
        2,
        'n != 1',
    ),
    (
        'anp',
        _('Angika'),
        2,
        'n != 1',
    ),
    (
        'ar',
        _('Arabic'),
        6,
        'n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5',
    ),
    (
        'ar_DZ',
        _('Arabic (Algeria)'),
        6,
        'n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5',
    ),
    (
        'ar_MA',
        _('Arabic (Morocco)'),
        6,
        'n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5',
    ),
    (
        'arn',
        _('Mapudungun'),
        2,
        'n > 1',
    ),
    (
        'ars',
        _('Najdi Arabic'),
        6,
        '(n == 0) ? 0 : ((n == 1) ? 1 : ((n == 2) ? 2 : ((n % 100 >= 3 && n % 100 <= 10) ? 3 : ((n % 100 >= 11 && n % 100 <= 99) ? 4 : 5))))',
    ),
    (
        'as',
        _('Assamese'),
        2,
        'n > 1',
    ),
    (
        'asa',
        _('Asu'),
        2,
        'n != 1',
    ),
    (
        'ast',
        _('Asturian'),
        2,
        'n != 1',
    ),
    (
        'av',
        _('Avaric'),
        2,
        'n != 1',
    ),
    (
        'ay',
        _('Aymará'),
        1,
        '0',
    ),
    (
        'az',
        _('Azerbaijani'),
        2,
        'n != 1',
    ),
    (
        'ba',
        _('Bashkir'),
        2,
        'n != 1',
    ),
    (
        'bar',
        _('Bavarian'),
        2,
        'n != 1',
    ),
    (
        'be',
        _('Belarusian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'be_Latn',
        _('Belarusian (latin)'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'bem',
        _('Bemba'),
        2,
        'n != 1',
    ),
    (
        'bez',
        _('Bena'),
        2,
        'n != 1',
    ),
    (
        'bg',
        _('Bulgarian'),
        2,
        'n != 1',
    ),
    (
        'bh',
        _('Bihari'),
        2,
        'n > 1',
    ),
    (
        'bi',
        _('Bislama'),
        2,
        'n != 1',
    ),
    (
        'bm',
        _('Bambara'),
        1,
        '0',
    ),
    (
        'bn',
        _('Bengali'),
        2,
        'n > 1',
    ),
    (
        'bn_BD',
        _('Bengali (Bangladesh)'),
        2,
        'n != 1',
    ),
    (
        'bn_IN',
        _('Bengali (India)'),
        2,
        'n != 1',
    ),
    (
        'bo',
        _('Tibetan'),
        1,
        '0',
    ),
    (
        'br',
        _('Breton'),
        5,
        '(n % 10 == 1 && n % 100 != 11 && n % 100 != 71 && n % 100 != 91) ? 0 : ((n % 10 == 2 && n % 100 != 12 && n % 100 != 72 && n % 100 != 92) ? 1 : ((((n % 10 == 3 || n % 10 == 4) || n % 10 == 9) && (n % 100 < 10 || n % 100 > 19) && (n % 100 < 70 || n % 100 > 79) && (n % 100 < 90 || n % 100 > 99)) ? 2 : ((n != 0 && n % 1000000 == 0) ? 3 : 4)))',
    ),
    (
        'brx',
        _('Bodo'),
        2,
        'n != 1',
    ),
    (
        'bs',
        _('Bosnian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'bs_Cyrl',
        _('Bosnian (cyrillic)'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'bs_Latn',
        _('Bosnian (latin)'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'byn',
        _('Bilen'),
        2,
        'n != 1',
    ),
    (
        'ca',
        _('Catalan'),
        2,
        'n != 1',
    ),
    (
        'ca@valencia',
        _('Valencian'),
        2,
        'n != 1',
    ),
    (
        'ce',
        _('Chechen'),
        2,
        'n != 1',
    ),
    (
        'ceb',
        _('Cebuano'),
        2,
        'n != 1',
    ),
    (
        'cgg',
        _('Chiga'),
        2,
        'n != 1',
    ),
    (
        'ch',
        _('Chamorro'),
        2,
        'n != 1',
    ),
    (
        'chm',
        _('Mari'),
        2,
        'n != 1',
    ),
    (
        'chr',
        _('Cherokee'),
        2,
        'n != 1',
    ),
    (
        'ckb',
        _('Sorani'),
        2,
        'n != 1',
    ),
    (
        'cmn',
        _('Chinese (Mandarin)'),
        1,
        '0',
    ),
    (
        'co',
        _('Corsican'),
        2,
        'n != 1',
    ),
    (
        'cr',
        _('Cree'),
        2,
        'n != 1',
    ),
    (
        'crh',
        _('Crimean Tatar'),
        1,
        '0',
    ),
    (
        'cs',
        _('Czech'),
        3,
        '(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2',
    ),
    (
        'csb',
        _('Kashubian'),
        3,
        'n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'cu',
        _('Old Church Slavonic'),
        2,
        'n != 1',
    ),
    (
        'cv',
        _('Chuvash'),
        2,
        'n != 1',
    ),
    (
        'cy',
        _('Welsh'),
        6,
        '(n==0) ? 0 : (n==1) ? 1 : (n==2) ? 2 : (n==3) ? 3 :(n==6) ? 4 : 5',
    ),
    (
        'da',
        _('Danish'),
        2,
        'n != 1',
    ),
    (
        'de',
        _('German'),
        2,
        'n != 1',
    ),
    (
        'de_AT',
        _('Austrian German'),
        2,
        'n != 1',
    ),
    (
        'de_CH',
        _('Swiss High German'),
        2,
        'n != 1',
    ),
    (
        'doi',
        _('Dogri'),
        2,
        'n != 1',
    ),
    (
        'dsb',
        _('Lower Sorbian'),
        4,
        '(n % 100 == 1) ? 0 : ((n % 100 == 2) ? 1 : ((n % 100 == 3 || n % 100 == 4) ? 2 : 3))',
    ),
    (
        'dv',
        _('Dhivehi'),
        2,
        'n != 1',
    ),
    (
        'dz',
        _('Dzongkha'),
        1,
        '0',
    ),
    (
        'ee',
        _('Ewe'),
        2,
        'n != 1',
    ),
    (
        'el',
        _('Greek'),
        2,
        'n != 1',
    ),
    (
        'en',
        _('English'),
        2,
        'n != 1',
    ),
    (
        'en_AU',
        _('English (Australia)'),
        2,
        'n != 1',
    ),
    (
        'en_CA',
        _('English (Canada)'),
        2,
        'n != 1',
    ),
    (
        'en_GB',
        _('English (United Kingdom)'),
        2,
        'n != 1',
    ),
    (
        'en_IE',
        _('English (Ireland)'),
        2,
        'n != 1',
    ),
    (
        'en_PH',
        _('English (Philippines)'),
        2,
        'n != 1',
    ),
    (
        'en_US',
        _('English (United States)'),
        2,
        'n != 1',
    ),
    (
        'en_ZA',
        _('English (South Africa)'),
        2,
        'n != 1',
    ),
    (
        'eo',
        _('Esperanto'),
        2,
        'n != 1',
    ),
    (
        'es',
        _('Spanish'),
        2,
        'n != 1',
    ),
    (
        'es_AR',
        _('Spanish (Argentina)'),
        2,
        'n != 1',
    ),
    (
        'es_CL',
        _('Spanish (Chile)'),
        2,
        'n != 1',
    ),
    (
        'es_EC',
        _('Spanish (Ecuador)'),
        2,
        'n != 1',
    ),
    (
        'es_MX',
        _('Spanish (Mexico)'),
        2,
        'n != 1',
    ),
    (
        'es_PR',
        _('Spanish (Puerto Rico)'),
        2,
        'n != 1',
    ),
    (
        'es_US',
        _('Spanish (American)'),
        2,
        'n != 1',
    ),
    (
        'et',
        _('Estonian'),
        2,
        'n != 1',
    ),
    (
        'eu',
        _('Basque'),
        2,
        'n != 1',
    ),
    (
        'fa',
        _('Persian'),
        2,
        'n > 1',
    ),
    (
        'fa_AF',
        _('Dari'),
        2,
        'n > 1',
    ),
    (
        'ff',
        _('Fulah'),
        2,
        'n > 1',
    ),
    (
        'fi',
        _('Finnish'),
        2,
        'n != 1',
    ),
    (
        'fil',
        _('Filipino'),
        2,
        'n != 1 && n != 2 && n != 3 && (n % 10 == 4 || n % 10 == 6 || n % 10 == 9)',
    ),
    (
        'fj',
        _('Fijian'),
        2,
        'n != 1',
    ),
    (
        'fo',
        _('Faroese'),
        2,
        'n != 1',
    ),
    (
        'fr',
        _('French'),
        2,
        'n > 1',
    ),
    (
        'fr_CA',
        _('French (Canada)'),
        2,
        'n > 1',
    ),
    (
        'fr_CH',
        _('French (Switzerland)'),
        2,
        'n > 1',
    ),
    (
        'frp',
        _('Franco-Provençal'),
        2,
        'n > 1',
    ),
    (
        'fur',
        _('Friulian'),
        2,
        'n != 1',
    ),
    (
        'fy',
        _('Frisian'),
        2,
        'n != 1',
    ),
    (
        'ga',
        _('Irish'),
        5,
        'n==1 ? 0 : n==2 ? 1 : (n>2 && n<7) ? 2 :(n>6 && n<11) ? 3 : 4',
    ),
    (
        'gd',
        _('Gaelic'),
        4,
        '(n==1 || n==11) ? 0 : (n==2 || n==12) ? 1 : (n > 2 && n < 20) ? 2 : 3',
    ),
    (
        'gez',
        _('Ge\'ez'),
        2,
        'n != 1',
    ),
    (
        'gl',
        _('Galician'),
        2,
        'n != 1',
    ),
    (
        'gn',
        _('Guarani'),
        2,
        'n != 1',
    ),
    (
        'gsw',
        _('Swiss German'),
        2,
        'n != 1',
    ),
    (
        'gu',
        _('Gujarati'),
        2,
        'n > 1',
    ),
    (
        'gun',
        _('Gun'),
        2,
        'n > 1',
    ),
    (
        'guw',
        _('Gun'),
        2,
        'n > 1',
    ),
    (
        'gv',
        _('Manx'),
        4,
        '(n % 10 == 1) ? 0 : ((n % 10 == 2) ? 1 : ((n % 100 == 0 || n % 100 == 20 || n % 100 == 40 || n % 100 == 60 || n % 100 == 80) ? 2 : 3))',
    ),
    (
        'ha',
        _('Hausa'),
        2,
        'n != 1',
    ),
    (
        'haw',
        _('Hawaiian'),
        2,
        'n != 1',
    ),
    (
        'he',
        _('Hebrew'),
        4,
        '(n == 1) ? 0 : ((n == 2) ? 1 : ((n > 10 && n % 10 == 0) ? 2 : 3))',
    ),
    (
        'hi',
        _('Hindi'),
        2,
        'n > 1',
    ),
    (
        'hil',
        _('Hiligaynon'),
        2,
        'n != 1',
    ),
    (
        'hne',
        _('Chhattisgarhi'),
        2,
        'n != 1',
    ),
    (
        'ho',
        _('Hiri Motu'),
        2,
        'n != 1',
    ),
    (
        'hr',
        _('Croatian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'hrx',
        _('Hunsrik'),
        2,
        'n != 1',
    ),
    (
        'hsb',
        _('Upper Sorbian'),
        4,
        '(n % 100 == 1) ? 0 : ((n % 100 == 2) ? 1 : ((n % 100 == 3 || n % 100 == 4) ? 2 : 3))',
    ),
    (
        'ht',
        _('Haitian'),
        2,
        'n != 1',
    ),
    (
        'hu',
        _('Hungarian'),
        2,
        'n != 1',
    ),
    (
        'hy',
        _('Armenian'),
        2,
        'n > 1',
    ),
    (
        'hz',
        _('Herero'),
        2,
        'n != 1',
    ),
    (
        'ia',
        _('Interlingua'),
        2,
        'n != 1',
    ),
    (
        'id',
        _('Indonesian'),
        1,
        '0',
    ),
    (
        'ie',
        _('Occidental'),
        2,
        'n != 1',
    ),
    (
        'ig',
        _('Igbo'),
        1,
        '0',
    ),
    (
        'ii',
        _('Nuosu'),
        1,
        '0',
    ),
    (
        'ik',
        _('Inupiaq'),
        2,
        'n != 1',
    ),
    (
        'io',
        _('Ido'),
        2,
        'n != 1',
    ),
    (
        'is',
        _('Icelandic'),
        2,
        'n % 10 != 1 || n % 100 == 11',
    ),
    (
        'it',
        _('Italian'),
        2,
        'n != 1',
    ),
    (
        'iu',
        _('Inuktitut'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'ja',
        _('Japanese'),
        1,
        '0',
    ),
    (
        'jam',
        _('Jamaican Patois'),
        2,
        'n != 1',
    ),
    (
        'jbo',
        _('Lojban'),
        1,
        '0',
    ),
    (
        'jgo',
        _('Ngomba'),
        2,
        'n != 1',
    ),
    (
        'jmc',
        _('Machame'),
        2,
        'n != 1',
    ),
    (
        'jv',
        _('Javanese'),
        1,
        '0',
    ),
    (
        'ka',
        _('Georgian'),
        2,
        'n != 1',
    ),
    (
        'kab',
        _('Kabyle'),
        2,
        'n > 1',
    ),
    (
        'kaj',
        _('Jju'),
        2,
        'n != 1',
    ),
    (
        'kcg',
        _('Tyap'),
        2,
        'n != 1',
    ),
    (
        'kde',
        _('Makonde'),
        1,
        '0',
    ),
    (
        'kea',
        _('Kabuverdianu'),
        1,
        '0',
    ),
    (
        'kg',
        _('Kongo'),
        2,
        'n != 1',
    ),
    (
        'ki',
        _('Gikuyu'),
        2,
        'n != 1',
    ),
    (
        'kj',
        _('Kwanyama'),
        2,
        'n != 1',
    ),
    (
        'kk',
        _('Kazakh'),
        2,
        'n != 1',
    ),
    (
        'kkj',
        _('Kako'),
        2,
        'n != 1',
    ),
    (
        'kl',
        _('Greenlandic'),
        2,
        'n != 1',
    ),
    (
        'km',
        _('Central Khmer'),
        1,
        '0',
    ),
    (
        'kmr',
        _('Kurmanji'),
        2,
        'n != 1',
    ),
    (
        'kn',
        _('Kannada'),
        2,
        'n > 1',
    ),
    (
        'ko',
        _('Korean'),
        1,
        '0',
    ),
    (
        'kok',
        _('Konkani'),
        2,
        'n != 1',
    ),
    (
        'kr',
        _('Kanuri'),
        2,
        'n != 1',
    ),
    (
        'ks',
        _('Kashmiri'),
        2,
        'n != 1',
    ),
    (
        'ksb',
        _('Shambala'),
        2,
        'n != 1',
    ),
    (
        'ksh',
        _('Colognian'),
        3,
        'n==0 ? 0 : n==1 ? 1 : 2',
    ),
    (
        'ku',
        _('Kurdish'),
        2,
        'n != 1',
    ),
    (
        'kv',
        _('Komi'),
        2,
        'n != 1',
    ),
    (
        'kw',
        _('Cornish'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'ky',
        _('Kyrgyz'),
        2,
        'n != 1',
    ),
    (
        'la',
        _('Latin'),
        2,
        'n != 1',
    ),
    (
        'lag',
        _('Langi'),
        3,
        '(n == 0) ? 0 : ((n == 1) ? 1 : 2)',
    ),
    (
        'lb',
        _('Luxembourgish'),
        2,
        'n != 1',
    ),
    (
        'lg',
        _('Luganda'),
        2,
        'n != 1',
    ),
    (
        'li',
        _('Limburgish'),
        2,
        'n != 1',
    ),
    (
        'lkt',
        _('Lakota'),
        1,
        '0',
    ),
    (
        'ln',
        _('Lingala'),
        2,
        'n > 1',
    ),
    (
        'lo',
        _('Lao'),
        1,
        '0',
    ),
    (
        'lt',
        _('Lithuanian'),
        3,
        '(n % 10 == 1 && (n % 100 < 11 || n % 100 > 19)) ? 0 : ((n % 10 >= 2 && n % 10 <= 9 && (n % 100 < 11 || n % 100 > 19)) ? 1 : 2)',
    ),
    (
        'lu',
        _('Luba-Katanga'),
        2,
        'n != 1',
    ),
    (
        'lv',
        _('Latvian'),
        3,
        '(n % 10 == 0 || n % 100 >= 11 && n % 100 <= 19) ? 0 : ((n % 10 == 1 && n % 100 != 11) ? 1 : 2)',
    ),
    (
        'mai',
        _('Maithili'),
        2,
        'n != 1',
    ),
    (
        'mas',
        _('Masai'),
        2,
        'n != 1',
    ),
    (
        'me',
        _('Montenegrin'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'mfe',
        _('Morisyen'),
        2,
        'n > 1',
    ),
    (
        'mg',
        _('Malagasy'),
        2,
        'n > 1',
    ),
    (
        'mgo',
        _('Metaʼ'),
        2,
        'n != 1',
    ),
    (
        'mh',
        _('Marshallese'),
        2,
        'n != 1',
    ),
    (
        'mhr',
        _('Meadow Mari'),
        2,
        'n != 1',
    ),
    (
        'mi',
        _('Maori'),
        2,
        'n > 1',
    ),
    (
        'mk',
        _('Macedonian'),
        2,
        'n==1 || n%10==1 ? 0 : 1',
    ),
    (
        'ml',
        _('Malayalam'),
        2,
        'n != 1',
    ),
    (
        'mn',
        _('Mongolian'),
        2,
        'n != 1',
    ),
    (
        'mni',
        _('Manipuri'),
        2,
        'n != 1',
    ),
    (
        'mnk',
        _('Mandinka'),
        3,
        'n==0 ? 0 : n==1 ? 1 : 2',
    ),
    (
        'mr',
        _('Marathi'),
        2,
        'n > 1',
    ),
    (
        'ms',
        _('Malay'),
        1,
        '0',
    ),
    (
        'mt',
        _('Maltese'),
        4,
        'n==1 ? 0 : n==0 || ( n%100>1 && n%100<11) ? 1 : (n%100>10 && n%100<20 ) ? 2 : 3',
    ),
    (
        'my',
        _('Burmese'),
        1,
        '0',
    ),
    (
        'na',
        _('Nauru'),
        2,
        'n != 1',
    ),
    (
        'nah',
        _('Nahuatl'),
        2,
        'n != 1',
    ),
    (
        'nap',
        _('Neapolitan'),
        2,
        'n != 1',
    ),
    (
        'naq',
        _('Nama'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'nb',
        _('Norwegian Bokmål'),
        2,
        'n != 1',
    ),
    (
        'nd',
        _('North Ndebele'),
        2,
        'n != 1',
    ),
    (
        'nds',
        _('Low German'),
        2,
        'n != 1',
    ),
    (
        'ne',
        _('Nepali'),
        2,
        'n != 1',
    ),
    (
        'ng',
        _('Ndonga'),
        2,
        'n != 1',
    ),
    (
        'nl',
        _('Dutch'),
        2,
        'n != 1',
    ),
    (
        'nl_BE',
        _('Flemish'),
        2,
        'n != 1',
    ),
    (
        'nn',
        _('Norwegian Nynorsk'),
        2,
        'n != 1',
    ),
    (
        'nnh',
        _('Ngiemboon'),
        2,
        'n != 1',
    ),
    (
        'nqo',
        _('N’Ko'),
        1,
        '0',
    ),
    (
        'nr',
        _('South Ndebele'),
        2,
        'n != 1',
    ),
    (
        'nso',
        _('Pedi'),
        2,
        'n > 1',
    ),
    (
        'nv',
        _('Navaho'),
        2,
        'n != 1',
    ),
    (
        'ny',
        _('Nyanja'),
        2,
        'n != 1',
    ),
    (
        'nyn',
        _('Nyankole'),
        2,
        'n != 1',
    ),
    (
        'oc',
        _('Occitan'),
        2,
        'n > 1',
    ),
    (
        'oj',
        _('Ojibwe'),
        2,
        'n != 1',
    ),
    (
        'om',
        _('Oromo'),
        2,
        'n != 1',
    ),
    (
        'or',
        _('Odia'),
        2,
        'n != 1',
    ),
    (
        'os',
        _('Ossetian'),
        2,
        'n != 1',
    ),
    (
        'pa',
        _('Punjabi'),
        2,
        'n > 1',
    ),
    (
        'pap',
        _('Papiamento'),
        2,
        'n != 1',
    ),
    (
        'pi',
        _('Pali'),
        2,
        'n != 1',
    ),
    (
        'pl',
        _('Polish'),
        3,
        'n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'pms',
        _('Piemontese'),
        2,
        'n != 1',
    ),
    (
        'pr',
        _('Pirate'),
        2,
        'n != 1',
    ),
    (
        'prg',
        _('Prussian'),
        3,
        '(n % 10 == 0 || n % 100 >= 11 && n % 100 <= 19) ? 0 : ((n % 10 == 1 && n % 100 != 11) ? 1 : 2)',
    ),
    (
        'ps',
        _('Pashto'),
        2,
        'n != 1',
    ),
    (
        'pt',
        _('Portuguese'),
        2,
        'n > 1',
    ),
    (
        'pt_BR',
        _('Portuguese (Brazil)'),
        2,
        'n > 1',
    ),
    (
        'pt_PT',
        _('Portuguese (Portugal)'),
        2,
        'n != 1',
    ),
    (
        'qu',
        _('Quechua'),
        2,
        'n != 1',
    ),
    (
        'rm',
        _('Romansh'),
        2,
        'n != 1',
    ),
    (
        'rn',
        _('Rundi'),
        2,
        'n != 1',
    ),
    (
        'ro',
        _('Romanian'),
        3,
        'n==1 ? 0 : (n==0 || (n%100 > 0 && n%100 < 20)) ? 1 : 2',
    ),
    (
        'ro_MD',
        _('Moldavian'),
        3,
        '(n == 1) ? 0 : ((n == 0 || n != 1 && n % 100 >= 1 && n % 100 <= 19) ? 1 : 2)',
    ),
    (
        'rof',
        _('Rombo'),
        2,
        'n != 1',
    ),
    (
        'ru',
        _('Russian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'rue',
        _('Rusyn'),
        2,
        'n != 1',
    ),
    (
        'rw',
        _('Kinyarwanda'),
        2,
        'n != 1',
    ),
    (
        'rwk',
        _('Rwa'),
        2,
        'n != 1',
    ),
    (
        'sa',
        _('Sanskrit'),
        3,
        'n==1 ? 0 : n==2 ? 1 : 2',
    ),
    (
        'sah',
        _('Yakut'),
        1,
        '0',
    ),
    (
        'saq',
        _('Samburu'),
        2,
        'n != 1',
    ),
    (
        'sat',
        _('Santali'),
        2,
        'n != 1',
    ),
    (
        'sc',
        _('Sardinian'),
        2,
        'n != 1',
    ),
    (
        'sco',
        _('Scots'),
        2,
        'n != 1',
    ),
    (
        'sd',
        _('Sindhi'),
        2,
        'n != 1',
    ),
    (
        'sdh',
        _('Southern Kurdish'),
        2,
        'n != 1',
    ),
    (
        'se',
        _('Northern Sami'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'seh',
        _('Sena'),
        2,
        'n != 1',
    ),
    (
        'ses',
        _('Koyraboro Senni'),
        1,
        '0',
    ),
    (
        'sg',
        _('Sango'),
        1,
        '0',
    ),
    (
        'shi',
        _('Tachelhit'),
        3,
        '(n == 0 || n == 1) ? 0 : ((n >= 2 && n <= 10) ? 1 : 2)',
    ),
    (
        'shn',
        _('Shan'),
        2,
        'n != 1',
    ),
    (
        'si',
        _('Sinhala'),
        2,
        'n > 1',
    ),
    (
        'sk',
        _('Slovak'),
        3,
        '(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2',
    ),
    (
        'sl',
        _('Slovenian'),
        4,
        'n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3',
    ),
    (
        'sm',
        _('Samoan'),
        2,
        'n != 1',
    ),
    (
        'sma',
        _('Southern Sami'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'smi',
        _('Sami'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'smj',
        _('Lule Sami'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'smn',
        _('Inari Sami'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'sms',
        _('Skolt Sami'),
        3,
        '(n == 1) ? 0 : ((n == 2) ? 1 : 2)',
    ),
    (
        'sn',
        _('Shona'),
        2,
        'n != 1',
    ),
    (
        'so',
        _('Somali'),
        2,
        'n != 1',
    ),
    (
        'son',
        _('Songhai languages'),
        1,
        '0',
    ),
    (
        'sq',
        _('Albanian'),
        2,
        'n != 1',
    ),
    (
        'sr',
        _('Serbian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'sr_Cyrl',
        _('Serbian (cyrillic)'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'sr_Latn',
        _('Serbian (latin)'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'ss',
        _('Swati'),
        2,
        'n != 1',
    ),
    (
        'ssy',
        _('Saho'),
        2,
        'n != 1',
    ),
    (
        'st',
        _('Southern Sotho'),
        2,
        'n != 1',
    ),
    (
        'su',
        _('Sundanese'),
        1,
        '0',
    ),
    (
        'sv',
        _('Swedish'),
        2,
        'n != 1',
    ),
    (
        'sw',
        _('Swahili'),
        2,
        'n != 1',
    ),
    (
        'sw_CD',
        _('Congo Swahili'),
        2,
        'n != 1',
    ),
    (
        'syr',
        _('Syriac'),
        2,
        'n != 1',
    ),
    (
        'szl',
        _('Silesian'),
        3,
        'n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'ta',
        _('Tamil'),
        2,
        'n != 1',
    ),
    (
        'te',
        _('Telugu'),
        2,
        'n != 1',
    ),
    (
        'teo',
        _('Teso'),
        2,
        'n != 1',
    ),
    (
        'tg',
        _('Tajik'),
        1,
        '0',
    ),
    (
        'th',
        _('Thai'),
        1,
        '0',
    ),
    (
        'ti',
        _('Tigrinya'),
        2,
        'n > 1',
    ),
    (
        'tig',
        _('Tigre'),
        2,
        'n != 1',
    ),
    (
        'tk',
        _('Turkmen'),
        2,
        'n != 1',
    ),
    (
        'tl',
        _('Tagalog'),
        2,
        'n != 1 && n != 2 && n != 3 && (n % 10 == 4 || n % 10 == 6 || n % 10 == 9)',
    ),
    (
        'tlh-qaak',
        _('Klingon (pIqaD)'),
        1,
        '0',
    ),
    (
        'tlh',
        _('Klingon'),
        1,
        '0',
    ),
    (
        'tn',
        _('Tswana'),
        2,
        'n != 1',
    ),
    (
        'to',
        _('Tongan'),
        1,
        '0',
    ),
    (
        'tr',
        _('Turkish'),
        2,
        'n != 1',
    ),
    (
        'ts',
        _('Tsonga'),
        2,
        'n != 1',
    ),
    (
        'tt',
        _('Tatar'),
        1,
        '0',
    ),
    (
        'tw',
        _('Twi'),
        2,
        'n != 1',
    ),
    (
        'ty',
        _('Tahitian'),
        2,
        'n != 1',
    ),
    (
        'tzm',
        _('Central Atlas Tamazight'),
        2,
        'n >= 2 && (n < 11 || n > 99)',
    ),
    (
        'ug',
        _('Uyghur'),
        2,
        'n != 1',
    ),
    (
        'uk',
        _('Ukrainian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'ur',
        _('Urdu'),
        2,
        'n != 1',
    ),
    (
        'ur_PK',
        _('Urdu (Pakistan)'),
        2,
        'n != 1',
    ),
    (
        'uz',
        _('Uzbek'),
        2,
        'n != 1',
    ),
    (
        'uz_Latn',
        _('Uzbek (latin)'),
        2,
        'n != 1',
    ),
    (
        've',
        _('Venda'),
        2,
        'n != 1',
    ),
    (
        'vec',
        _('Venetian'),
        2,
        'n != 1',
    ),
    (
        'vi',
        _('Vietnamese'),
        1,
        '0',
    ),
    (
        'vls',
        _('West Flemish'),
        2,
        'n != 1',
    ),
    (
        'vo',
        _('Volapük'),
        2,
        'n != 1',
    ),
    (
        'vun',
        _('Vunjo'),
        2,
        'n != 1',
    ),
    (
        'wa',
        _('Walloon'),
        2,
        'n > 1',
    ),
    (
        'wae',
        _('Walser German'),
        2,
        'n != 1',
    ),
    (
        'wal',
        _('Wolaytta'),
        2,
        'n != 1',
    ),
    (
        'wen',
        _('Sorbian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'wo',
        _('Wolof'),
        1,
        '0',
    ),
    (
        'xh',
        _('Xhosa'),
        2,
        'n != 1',
    ),
    (
        'xog',
        _('Soga'),
        2,
        'n != 1',
    ),
    (
        'yi',
        _('Yiddish'),
        2,
        'n != 1',
    ),
    (
        'yo',
        _('Yoruba'),
        1,
        '0',
    ),
    (
        'yue',
        _('Yue'),
        1,
        '0',
    ),
    (
        'za',
        _('Zhuang'),
        2,
        'n != 1',
    ),
    (
        'zh',
        _('Chinese'),
        1,
        '0',
    ),
    (
        'zh_Hans',
        _('Chinese (Simplified)'),
        1,
        '0',
    ),
    (
        'zh_Hant',
        _('Chinese (Traditional)'),
        1,
        '0',
    ),
    (
        'zh_Hant_HK',
        _('Chinese (Hong Kong)'),
        1,
        '0',
    ),
    (
        'zu',
        _('Zulu'),
        2,
        'n > 1',
    ),
)

# Additional plural rules definitions
EXTRAPLURALS = (
    (
        'br',
        _('Breton'),
        2,
        'n > 1',
    ),
    (
        'cgg',
        _('Chiga'),
        1,
        '0',
    ),
    (
        'cy',
        _('Welsh'),
        2,
        '(n==2) ? 1 : 0',
    ),
    (
        'cy',
        _('Welsh'),
        4,
        '(n==1) ? 0 : (n==2) ? 1 : (n != 8 && n != 11) ? 2 : 3',
    ),
    (
        'dsb',
        _('Lower Sorbian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'fil',
        _('Filipino'),
        2,
        '(n > 1)',
    ),
    (
        'ga',
        _('Irish'),
        3,
        'n==1 ? 0 : n==2 ? 1 : 2',
    ),
    (
        'he',
        _('Hebrew'),
        2,
        '(n != 1)',
    ),
    (
        'he',
        _('Hebrew'),
        3,
        'n==1 ? 0 : n==2 ? 2 : 1',
    ),
    (
        'hsb',
        _('Upper Sorbian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'jv',
        _('Javanese'),
        2,
        '(n != 1)',
    ),
    (
        'ka',
        _('Georgian'),
        1,
        '0',
    ),
    (
        'kw',
        _('Cornish'),
        4,
        '(n==1) ? 0 : (n==2) ? 1 : (n == 3) ? 2 : 3',
    ),
    (
        'lt',
        _('Lithuanian'),
        4,
        'n==1 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : n%10==0 || (n%100>10 && n%100<20) ? 2 : 3',
    ),
    (
        'lt',
        _('Lithuanian'),
        3,
        '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)',
    ),
    (
        'lv',
        _('Latvian'),
        3,
        'n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2',
    ),
    (
        'lv',
        _('Latvian'),
        3,
        '(n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2)',
    ),
    (
        'se',
        _('Northern Sami'),
        2,
        '(n != 1)',
    ),
    (
        'sl',
        _('Slovenian'),
        4,
        '(n%100==1 ? 1 : n%100==2 ? 2 : n%100==3 || n%100==4 ? 3 : 0)',
    ),
)
