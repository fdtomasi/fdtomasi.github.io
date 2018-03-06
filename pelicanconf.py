#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Federico Tomasi'
SITENAME = u"Federico Tomasi"
SITEURL = ''
SITESUBTITLE = "[Personal Web Page]"

PATH = 'content'

TIMEZONE = 'Europe/Rome'
LOCALE = ('gb', 'en_GB', 'usa', 'en_US', 'en_GB.utf8')
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/fede.tomatoma'),
    ('twitter', 'https://twitter.com/kslw_'),
    ('instagram', 'https://www.instagram.com/klsw_/'),
    ('google-plus', 'https://plus.google.com/u/1/108368396270480629290'),
    ('youtube', 'https://www.youtube.com/channel/UCcRYAdfZQ_jj-Q9yirpbbbQ'),
    ('github', 'https://github.com/fdtomasi'),
          )
# SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = 1
# <li><a class="icon fa-facebook" href="https://www.facebook.com/fede.tomatoma"></a></li>
# <li><a class="icon fa-twitter" href="https://twitter.com/kslw_"></a></li>
# <li><a class="icon fa-instagram" href="https://www.instagram.com/klsw_/"></a></li>
# <li><a class="icon fa-google-plus" href="https://plus.google.com/u/1/108368396270480629290"></a></li>
# <li><a class="icon fa-youtube" href="https://www.youtube.com/channel/UCcRYAdfZQ_jj-Q9yirpbbbQ"></a></li>
# <li><a class="icon fa-github" href="https://github.com/fdtomasi"></a></li>

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')


PLUGIN_PATHS = ['./plugins']

# Other plugins:
# photos
import sys
sys.path.append("/home/fede/src/pelican-plugins")
import photos

PLUGINS = ['ipynb.markup', 'pelican-btex', 'jinja2content', 'pelican-ert',
           'neighbors', "render_math", photos]

# IPYNB_IGNORE_CSS=True

THEME = "/home/fede/pelican-themes/pelican-clean-blog"
# COLOR_SCHEME_CSS = 'redly.css'
# CSS_OVERRIDE = 'theme/css/ft-main.css'
CSS_OVERRIDE = 'extra/redly.css'
FOOTER_INCLUDE = 'ft-footer.html'
EXTRA_TEMPLATES_PATHS = [os.path.dirname(__file__)]
# GITHUB_URL = 'http://github.com/fdtomasi'

# HEADER_COLOR = 'white'
# HEADER_COVER = '<immagine>'

MENUITEMS = (
    # ("HOME", '/'),
    ("BIO", '/pages/bio.html'),
    ("TALKS", '/pages/talks.html'),
    ("RESEARCH", '/pages/research.html'),
    ("PUBLICATIONS", '/pages/publications.html'),
    ("SOFTWARE", '/pages/software.html'),
    ("LINKS", '/pages/links.html'),
)
DISPLAY_PAGES_ON_MENU = 0  # avoid duplicates
# SHOW_FULL_ARTICLE = True

STATIC_PATHS = [
    'images',
    'photos',
    'extra',
    'older'
]
# avoid to process such html
PAGE_EXCLUDES = ['older']
ARTICLE_EXCLUDES = ['older']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

ERT_WPM = 180  # words per minute by default
ERT_FORMAT = '{time} read'
MULTI_NEIGHBORS = 5
CC_LICENSE = "CC-BY-NC-SA"
BR_AFTER_IMG = True
