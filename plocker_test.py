import unittest
from plocker import User

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
        
        
        
        


if __name__ == '__main__':
    unittest.main()