import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test Class to test all the functionality of user class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        set up method to run before each test classes.
        '''

        self.new_user = User("Bella","Amandine","password","password")

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.fname, "Bella")
        self.assertEqual(self.new_user.lname, "Amandine")
        self.assertEqual(self.new_user.password, "password")
        self.assertEqual(self.new_user.confirmPassword, "password")

    def test_save_user(self):
        '''
        Test case to test if the user is saved into the list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
