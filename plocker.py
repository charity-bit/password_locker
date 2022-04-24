from random import randint


class User:
    
    '''
    Class that generates new instances of User
    '''
    users = []
    
    
    def __init__(self,username,password):
        '''
        define properties for our User objects
        '''
        self.username = username
        self.password = password
     
     
     
    
   
    def save_user(self):
        '''
        instance method user to save the user
        save user in user_list
        '''  
        User.users.append(self)
      
      
    '''
    remove users in user_list
    '''   
    def remove_user(self):
        User.users.remove(self)
        
    
class Credentials:
    '''
    Class that generates new instances of Credentials
    '''
    
    
    
    '''
    list to store our credentials
    '''
    creds_list = []
    
    
    
    def __init__(self,site_name,username,password):
        '''
        define properties for our Credential objects
        '''
        self.site_name = site_name
        self.username = username
        self.password = password
        
    def save_creds(self):
        '''
        method to save a credential
        '''
        Credentials.creds_list.append(self)
        
    
    
    def remove_cred(self):
        '''
        method to remove credential
    
        '''
        Credentials.creds_list.remove(self) 
    
        
   
    def update_cred(self):
         '''
         update credential
         '''
         return self
        
      
    
    @classmethod
    def aunthenticate(cls,username,password):
        '''
        method to check if user exists in users
        '''  
        active_user = ""
        for user in User.users:
            if (user.username == username and user.password == password):
                active_user = user.username
                
        return active_user
    
    
    @classmethod
    def display_creds(cls):
        '''
        return a list of all credentials 
        '''
        return cls.creds_list
    
   
    @classmethod
    def search_cred(cls,site_name):
        '''
        search for credential by name
        '''
        for cred in cls.creds_list:
            if cred.site_name == site_name:
                return cred
        
    
    def generate_password(ln):
        '''
        generate random password method
        '''
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890=?!#/@~$*"
        password = " "
        for i in range(ln):
            password += chars[randint(0, len(chars) - 1)]
        return password

        
        
    
        
        
    