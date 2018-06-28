import feedparser


class RSS:
    def __init__(self, url):
        self.url = feedparser.parse(url)

    def show_title_and_link(self):
        a = {}
        for entry in self.url.entries:
            a[entry.title] = entry.link

        return a
