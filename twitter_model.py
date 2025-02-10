class TweetModel:
    def __init__(self):
        self.user_name = ""
        self.user_fallowers = ""
        self.user_friends = ""
        self.user_favorites = ""

    def get_user_name(self):
        return self.user_name
    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_user_fallowers(self):
        return self.user_fallowers
    def set_user_fallowers(self, user_fallowers):
        self.user_fallowers = user_fallowers

    def get_user_friends(self):
        return self.user_friends
    def set_user_friends(self, user_friends):
        self.user_friends = user_friends

    def get_user_favorites(self):
        return self.user_favorites
    def set_user_favorites(self, user_favorites):
        self.user_favorites = user_favorites
    
    def __str__(self):
        return f"TweetModel{{username='{self.user_name}', user_fallowers = '{self.user_fallowers}', user_friends= '{self.user_friends}', user_favorites='{self.user_favorites}'}}"