import feedparser


class RSS:
    def __init__(self, url):
        self.url = feedparser.parse(url)

    def show_titles(self):
        a = {}
        for entry in self.url.entries:
            a[entry.title] = entry.link

        return a
