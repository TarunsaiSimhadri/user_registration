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


if __name__ == "__main__":
    unittest.main()

