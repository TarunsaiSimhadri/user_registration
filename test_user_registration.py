"""

@Author: TarunSai
@Date: 2024-07-23
@Last Modified by:
@Last Modified time: 
@Title : Test-cases for User Registration.

"""


import user_registration
import unittest


class TestUserRegistration(unittest.TestCase):

    def test_validate_first_name(self):
        self.assertTrue(user_registration.validate_first_name("Tarun"))
        self.assertFalse(user_registration.validate_first_name("tarun"))
    
    def test_validate_first_name(self):
        self.assertTrue(user_registration.validate_last_name("Tarun"))
        self.assertFalse(user_registration.validate_last_name("tarun"))

    def test_validate_email(self):
        self.assertTrue(user_registration.validate_email("abc@yahoo.com"))
        self.assertTrue(user_registration.validate_email("abc-100@yahoo.com"))
        self.assertTrue(user_registration.validate_email("abc.100@yahoo.com"))
        self.assertTrue(user_registration.validate_email("abc111@abc.com"))
        self.assertTrue(user_registration.validate_email("abc111@abc.net"))
        self.assertTrue(user_registration.validate_email("abc.100@abc.com.au"))
        self.assertTrue(user_registration.validate_email("abc@1.com"))
        self.assertTrue(user_registration.validate_email("abc@gmail.com.com"))
        self.assertTrue(user_registration.validate_email("abc+100@gmail.com"))

        self.assertFalse(user_registration.validate_email("abc"))
        self.assertFalse(user_registration.validate_email("abc.com.my"))
        self.assertFalse(user_registration.validate_email("abc123@gmail.a"))
        self.assertFalse(user_registration.validate_email("abc123@.com"))
        self.assertFalse(user_registration.validate_email("abc()*@gmail.com"))
        self.assertFalse(user_registration.validate_email("abc@%*.com"))
        self.assertFalse(user_registration.validate_email("abc@abc@gmail.com"))
        self.assertFalse(user_registration.validate_email("abc@gmail.com.1a"))

    def test_validate_mobile_no(self):
        self.assertTrue(user_registration.validate_mobile_no("92 9898989898"))
        self.assertFalse(user_registration.validate_mobile_no("91 989898989"))
        self.assertFalse(user_registration.validate_mobile_no("912 989898989"))

    def test_validate_password(self):
        self.assertTrue(user_registration.validate_password("tarunsai"))
        self.assertFalse(user_registration.validate_password("91 9898"))
        self.assertFalse(user_registration.validate_password("98989"))



if __name__ == "__main__":
    unittest.main()

