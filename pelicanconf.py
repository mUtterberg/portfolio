#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marissa Utterberg'
SITENAME = 'Utterberg Data & Development'
SITEURL = 'localhost:8000'
FAVICON = SITEURL + '/images/favicon.ico'
COPYRIGHT_YEAR = 2018

THEME = 'html5-dopetrope'

PATH = 'content'

STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

PLUGINS_PATHS = []
PLUGINS = []

ARTICLE_PATHS = ['articles',]

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Demo1', 'http://getpelican.com/'),
         ('Demo2', 'http://python.org/'),
         ('Demo3', 'http://jinja.pocoo.org/'),
         ('Demo4', '#'),)

# Social widget
SOCIAL = (('github', 'https://www.github.com/mutterberg/'),
          ('twitter', 'https://www.twitter.com/mutterberg/'),)

DEFAULT_PAGINATION = 10

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

# DEFAULT_METADATA = {
#     'status': 'draft',
# }

DELETE_OUTPUT_DIRECTORY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True