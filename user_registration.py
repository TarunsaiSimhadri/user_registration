"""

@Author: TarunSai
@Date: 2024-07-19
@Last Modified by:
@Last Modified time: 
@Title : User Registration.

"""


import re
from logger import get_logger

def validate_first_name(first_name):
  
    """
    description:
        Validates the first name.

    parameters:
        first_name: The first name to validate.

    Returns:
        True if the first name is valid, False otherwise.
    """

    if not first_name[0].isupper():
        return False
    if len(first_name) < 3:
        return False
    return True

def validate_last_name(last_name):

    """
    description:
        Validates the last name.

    parameters:
        last_name: The last name to validate.

    Returns:
        True if the last name is valid, False otherwise.
    """
      
    if not last_name[0].isupper():
        return False
    if len(last_name) < 3:
        return False
    return True

def validate_email(email):

    """
    description:
        Validates the email.

    parameters:
        email: The email to validate.

    Returns:
        True if the email is valid, False otherwise.
    """

    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" 
    match = re.match(regex, email)
    
    if match:
        return True
    return False


def main():

    while True:
        first_name = input("Enter a valid first name: ")
        logger = get_logger("validate_first_name")
        if validate_first_name(first_name):
            logger.info("first_name registered successfully")
            break
        else:
            logger.info("Invalid first name. Please try again.")

    while True:
        last_name = input("Enter a valid last name: ")
        logger = get_logger("validate_last_name")
        if validate_last_name(last_name):
            logger.info("last_name registered successfully")
            break
        else:
            logger.info("Invalid last name. Please try again.")

    while True:
        email = input("enter email id: ")
        logger = get_logger("validate_email")
        if validate_email(email):
            logger.info("email registered successfully")
            break
        else:
            logger.info("Invalid email. Please try again")


if __name__ == '__main__':
    main()

        
        
