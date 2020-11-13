import unittest
from cridential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test Class to test all the functionality of credential class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setup(self):
        '''
        set up method to run before each test case
        '''
        self.new_credential = Credential("insta", "1234")

    def tearDown(self):
        '''
        test case to run after each test case
        '''
        Credential.credential_list = []