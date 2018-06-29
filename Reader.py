import feedparser


class RSS:
    def __init__(self, url):
        self.url = feedparser.parse(url)

    def show_title_and_link(self):
        value_dict = {}
        for entry in self.url.entries:
            value_dict[entry.title] = entry.link

        return value_dict

    def show_more_details(self):
        value_list = []
        for entry in self.url.entries:
            value_list.append([entry.updated, entry.author, entry.title])

        return value_list
