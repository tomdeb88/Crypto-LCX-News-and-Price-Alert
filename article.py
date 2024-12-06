
class Article:
    def __init__(self,a_source,a_author,a_title,a_description,a_link):
        self.source=a_source
        self.author=a_author
        self.title=a_title
        self.description=a_description
        self.link=a_link

    def get_article(self):
        return (f"{self.source} author: {self.author}\nTitle: {self.title}\n"
                f"{self.description}\n"
                f"{self.link}\n")


