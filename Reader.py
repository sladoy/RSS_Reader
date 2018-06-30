import feedparser


class RSS:
    def __init__(self, url):
        self.url = feedparser.parse(url)

    def show_title_and_link(self):
        '''Get values from RSS'''
        value_dict = {}
        for entry in self.url.entries:
            value_dict[entry.title] = entry.link

        return value_dict

    def show_more_details(self):
        '''Get values from RSS'''
        value_list = []
        for entry in self.url.entries:
            value_list.append([entry.title, entry.author, entry.updated])

        return value_list
