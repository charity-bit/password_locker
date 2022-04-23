class User:
    users = []
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
        
    def save_user(self):
        User.users.append(self)
        
    def remove_user(self):
        User.users.remove(self)