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
from django.utils import timezone
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
                
                # When Story is attached to Plan, can get pubDate in the future 
                # and RSS feeds don't care for that ... 
                #
                # Using django timezone.now() instead of datetime.now() as 
                # timezone.now () is timzone aware and datetime.now() isn't.
                # http://stackoverflow.com/questions/10652819/django-1-4-cant-compare-offset-naive-and-offset-aware-datetimes
                if timestamp > timezone.now():
                    timestamp = timezone.now()
            else:
                timestamp = datetime.now()
            
            self.create_story(
                entry.link,
                title=entry.title,
                body=entry.description,
                timestamp=timestamp,
            )
