__author__ = 'nadav'


class Post:

    def __init__(self, author, message, group,created_time):
        self.author = author
        self.message = message
        self.group = group
        self.created_time = created_time

    def getAuthor(self):
        return self.author

    def getMessage(self):
        return self.message

    def getGroup(self):
        return self.group

    def getCreatedTime(self):
        return self.created_time