import unittest
from cridential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test Class to test all the functionality of credential class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        set up method to run before each test case
        '''
        self.new_credential = Credential("insta", "1234")

    def tearDown(self):
        '''
        test case to run after each test case
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        test case to test if the credential object is initialized
        '''
        self.assertEqual(self.new_credential.account_name, "insta")
    
    def test_save_credential(self):
        '''
        Test case to test if a new credential is saved into the list
        '''

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)


if __name__ == "__main__":
    unittest.main()