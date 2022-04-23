import unittest
from plocker import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("charity",'qwertyip')
        
    def test_init(self):
        self.assertEqual(self.new_user.username,"charity")
        self.assertEqual(self.new_user.password,"qwertyip")
        
        


if __name__ == '__main__':
    unittest.main()