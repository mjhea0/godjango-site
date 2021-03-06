from datetime import datetime

from django.contrib.syndication.views import Feed

from episode.models import Video

class LatestVideos(Feed):
        title = "GoDjango Screencasts"
        link = "https://godjango.com"
        description = "Screencast covering some topic about Django."

        def items(self):
            return Video.objects.filter(publish_date__lte=datetime.now()).filter(is_premium__exact=False).order_by('-publish_date')[:20]

        def item_title(self, item):
            return item.title

        def item_description(self, item):
            return item.description + ("<br /><a href='https://godjango.com%s'>Watch Now...</a>" % (item.get_absolute_url()))

        def item_link(self, item):
            return item.get_absolute_url()

        def item_pubdate(self, item):
            return item.publish_date
