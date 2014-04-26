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
import pytz
import time

from newswall.providers.base import ProviderBase

class Provider(ProviderBase):
    def update(self):
        feed = feedparser.parse(self.config['source'])
        
        for entry in feed['entries']:
            if hasattr(entry, 'date_parsed'):
                # set tm_isdst=1 on time.struct_time( ... ) here
                timestamp = datetime.fromtimestamp(
                    time.mktime(entry.date_parsed))
            elif hasattr(entry, 'published_parsed'):
                # set tm_isdst=1 on time.struct_time( ... ) here
                timestamp = datetime.fromtimestamp(
                    time.mktime(entry.published_parsed))
            else:
                timestamp = datetime.now()
            
            timestamp = timestamp.replace(tzinfo=pytz.utc)
            
            self.create_story(
                entry.link,
                title=entry.title,
                body=entry.description,
                timestamp=timestamp,
            )
