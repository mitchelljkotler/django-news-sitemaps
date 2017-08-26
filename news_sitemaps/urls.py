from django.conf.urls import *

from news_sitemaps import registry, views


urlpatterns = [
    url(r'^index\.xml$',
        views.index,
        {'sitemaps': registry},
        name='news_sitemaps_index'),

    url(r'^(?P<section>.+)\.xml',
        views.news_sitemap,
        {'sitemaps': registry},
        name='news_sitemaps_sitemap'),
]
