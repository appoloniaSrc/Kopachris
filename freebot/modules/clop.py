#!/usr/bin/env python
# coding: utf8
from gluon import *
import bot_utils
import urllib2
import json
#from bs4 import BeautifulSoup

## Description stored in db.bot_modules
# returned by !help command
description = "!clop - Gets random clop image from derpibooru API"

## Prefix stored in db.bot_modules
## Each module should have its own prefix for bot_vars entries
prefix = "clop_"

## Event type handled by this module
# multiple event types not supported yet
event_type = "PRIVMSG"

## Additional global vars go here

# a lot of websites block specific user-agent strings associated with bots
# use this to avoid that if your module retrieves webpages
H_HTTP = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
D_URL = 'http://derpiboo.ru/search.json?q=explicit%2C+-gore%2C+-grimdark%2C+-foalcon%2C+-scat%2C+-bestiality&random_image=y&min_score=100&key=<apikey>'
#D_URL = 'https://derpiboo.ru/search.json?q=%28explicit+OR+questionable+OR+suggestive%29%2C+-gore%2C+-grimdark&random_image=y&min_score=100'
D_GET = {'q': 'explicit, -gore, -grimdark',
         'random_image': 'y',
         'min_score': 100,
         }

def init(db):
    # called when module is uploaded/enabled
    # create any tables or add default values to db.bot_vars
    pass


def remove(db):
    # called when module is disabled
    pass


def run(bot, event, db):
    mod_name = __name__.rsplit('.', 1)[1]
    this_mod = db(db.bot_modules.name == mod_name).select()
    prefix = this_mod.first().vars_pre
    m_items = prefix + "items"
    bot_nick = bot.nickname
    
    m = event.message.lower()
    
    if m.startswith('!clop'):
        # general form for identifying a command
        req = urllib2.Request(D_URL, headers=H_HTTP)
        id = json.loads(urllib2.urlopen(req).read())['id']
        bot.bot_reply(event, 'CLOP CLOP CLOP https://derpiboo.ru/' + str(id), False)
