class SocialMediaAccount:
    def __init__(self, username, password):
        self.password = username
        self.password = password
    def login():
       pass
    def past ():
        pass
   
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, num_follow):
        super().__init__(username, password)
        self.num_follow = num_follow
    def share_story():
        pass
 
class XAaccount(SocialMediaAccount):
    def __init__(self, username, password, num_tweett):
        super().__init__(username, password)
        self.num_tweett = num_tweett
    def tweet():
        pass

