"""
RSS Feed Provider
=================

Required configuration keys::

    {
    "provider": "newswall.providers.feed",
    "source": "http://twitter.com/statuses/user_timeline/feinheit.rss"
    }
"""
from datetime import datetime
import feedparser
from dateutil import parser
import time

from newswall.providers.base import ProviderBase

class Provider(ProviderBase):
    def update(self):
        feed = feedparser.parse(self.config['source'])
        
        for entry in feed['entries']:
            if hasattr(entry, 'published'):
                # Most helpful! http://stackoverflow.com/questions/20867795/python-how-to-get-timezone-from-rss-feed
                timestamp = parser.parse(entry.published)
            else:
                timestamp = datetime.now()
            
            self.create_story(
                entry.link,
                title=entry.title,
                body=entry.description,
                timestamp=timestamp,
            )
