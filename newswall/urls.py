from django.conf.urls import url, patterns

from newswall.feeds import StoryFeed
from newswall import views

urlpatterns = patterns(
    '',
    url(r'^feed/$', StoryFeed()),
    url(r'^$',
        views.ArchiveIndexView.as_view(),
        name='newswall_entry_archive'),
    url(r'^index/$',
        views.ArchiveIndexView.as_view(),
        name='newswall_entry_index'),
    url(r'^(?P<year>\d{4})/$',
        views.YearArchiveView.as_view(),
        name='newswall_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.MonthArchiveView.as_view(),
        name='newswall_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        views.DayArchiveView.as_view(),
        name='newswall_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.DateDetailView.as_view(),
        name='newswall_entry_detail'),
    url(r'^source/(?P<slug>[-\w]+)/$',
        views.SourceArchiveIndexView.as_view(),
        name='newswall_source_detail'),
    url(r'^basketball/$',
        views.BasketballArchiveIndexView.as_view(),
        name='doApp_basketball'),
    url(r'^latest/$',
        views.LatestLocalIndexView.as_view(),
        name='homepage_local'),
)
