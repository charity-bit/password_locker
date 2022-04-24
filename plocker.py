from random import randint


class User:
    
    '''
    Class that generates new instances of User
    '''
    users = []
    
    '''
    define properties for our User objects
    '''
    def __init__(self,username,password):
        self.username = username
        self.password = password
     
     
    '''
    instance method user to save the user
    '''   
    
    '''
    save user in user_list
    '''
    def save_user(self):
        User.users.append(self)
      
      
    '''
    remove users in user_list
    '''   
    def remove_user(self):
        User.users.remove(self)
        
    
class Credentials:
    
    
    '''
    list to store our credentials
    '''
    creds_list = []
    
    '''
    Class that generates new instances of Credentials
    '''
    
    '''
    define properties for our Credential objects
    '''
    def __init__(self,site_name,username,password):
        self.site_name = site_name
        self.username = username
        self.password = password
        
    def save_creds(self):
        Credentials.creds_list.append(self)
        
    '''
    method to remove credential
    
    '''
    
    def remove_cred(self):
        Credentials.creds_list.remove(self) 
    
        
    '''
    update credential
    '''
    def update_cred(self):
        return self
        
      
    '''
    method to check if user exists in users
    '''  
    @classmethod
    def aunthenticate(cls,username,password):
        active_user = ""
        for user in User.users:
            if (user.username == username and user.password == password):
                active_user = user.username
                
        return active_user
    
    '''
    return a list of all credentials 
    '''
    @classmethod
    def display_creds(cls):
        return cls.creds_list
    
    '''
    search for credential by name
    '''
    @classmethod
    def search_cred(cls,site_name):
        for cred in cls.creds_list:
            if cred.site_name == site_name:
                return cred
        
    '''
    generate random password method
    '''
    def generate_pasword(ln):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*!#$@?&/=|"
        pwd = ""
        for i in range(len):
            pwd += chars[randint(0, len(chars) - 1)] #generate random int from 0 to last index of chars
            
        return pwd
        
        
    
        
        
    