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
        
        


if __name__ == '__main__':
    unittest.main()