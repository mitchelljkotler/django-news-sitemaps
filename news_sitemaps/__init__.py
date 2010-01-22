from django.contrib.sitemaps import Sitemap

class NewsSitemap(Sitemap):
    def genres(self, obj):
        """
        Returns a comma-separated list of properties characterizing the content of the article,
        such as "PressRelease" or "UserGenerated." Your content must be labeled accurately,
        in order to provide a consistent experience for our users.
        
        Options are::
        
            * PressRelease (visible): an official press release.
            * Satire (visible): an article which ridicules its subject for didactic purposes.
            * Blog (visible): any article published on a blog, or in a blog format.
            * OpEd: an opinion-based article which comes specifically from the Op-Ed section of your site.
            * Opinion: any other opinion-based article not appearing on an Op-Ed page, i.e., reviews, interviews, etc.
            * UserGenerated: newsworthy user-generated content which has already gone through a formal editorial review process on your site.
        """
        return 'PressRelease'
    
    def title(self, obj):
        """
        Returns the title of the news article.
        Note: The title may be truncated for space reasons when shown on Google News.
        """
        if hasattr(obj, 'title'):
            return obj.title
        elif hasattr(obj, 'name'):
            return obj.name
        elif hasattr(obj, 'headline'):
            return obj.headline
        return ''
    
    def keywords(self, obj):
        """
        Returns a comma-separated list of keywords describing the topic of the article.
        Keywords may be drawn from, but are not limited to, the list of existing Google News keywords.
        """
        if hasattr(obj, 'keywords'):
            return obj.keywords
        elif hasattr(obj, 'tags'):
            return obj.tags
        return ''
    
    def access(self, obj):
        """
        Returns description of the accessibility of the article.
        If the article is accessible to Google News readers without a registration or subscription,
        this function should return None
        
        Options are::
        
            * Subscription (visible): an article which prompts users to pay to view content.
            * Registration (visible): an article which prompts users to sign up for an unpaid account to view content.
        """
        return None
        
    def get_urls(self, page=1):
        from django.contrib.sites.models import Site
        current_site = Site.objects.get_current()
        urls = []
        for item in self.paginator.page(page).object_list:
            loc = "http://%s%s" % (current_site.domain, self._Sitemap__get('location', item))
            url_info = {
                'location':   loc,
                'lastmod':    self._Sitemap__get('lastmod', item, None),
                'changefreq': self._Sitemap__get('changefreq', item, None),
                'priority':   self._Sitemap__get('priority', item, None),
                
                # News attrs
                'access':     self._Sitemap__get('access', item, None),
                'keywords':   self._Sitemap__get('keywords', item, None),
                'genres':     self._Sitemap__get('genres', item, None),
                'title':      self._Sitemap__get('title', item, None),
            }
            urls.append(url_info)
        return urls