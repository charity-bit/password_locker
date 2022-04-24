import unittest
from plocker import Credentials, User

class TestUser(unittest.TestCase):
    
    '''
    set up method to run before each test
    create a new user before any test
    '''
    def setUp(self):
        self.new_user = User("charity",'qwertyip')
        
        
    '''
    test_init to test if the object is initialized properly
    
    '''
    def test_init(self):
        self.assertEqual(self.new_user.username,"charity")
        self.assertEqual(self.new_user.password,"qwertyip")
      
      
    '''
    unit test to test if a user has been saved successfully
    '''  
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)
        
    def tearDown(self):
        '''
         clean users array after every test
        '''
        User.users = []
        
    def test_remove_user(self):
        self.new_user.save_user()
        test_user = User("nyanchera","12345")
        test_user.save_user()
        self.new_user.remove_user()
        self.assertEqual(len(User.users),1)
    
class TestCredential(unittest.TestCase):
    '''
     Unitest for the credential class
    '''
    
    def setUp(self):
        '''
        set up Method to create a new cred before every test
        '''
        
        new_cred = Credentials("twitter","Ccnyanchera","qwertyip")
    def tearDown(self):
        '''
        clear the creds lists after every test
        '''
        Credentials.creds_list = []
    
    def test_save_creds(self):
        self.new_creds.save_creds()
        
        
        


if __name__ == '__main__':
    unittest.main()