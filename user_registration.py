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

def validate_mobile_no(mobile_no):

    """
    description:
        Validates the mobile no.

    parameters:
        mobile no: The mobile no to validate.

    Returns:
        True if the mobile no is valid, False otherwise.
    """

    regex = r"^\d{2} \d{10}$"
    match = re.match(regex, mobile_no)
    
    if match:
        return True
    return False

def validate_password(password):

    """
    description:
        Validates the password.

    parameters:
        password: The password to validate.

    Returns:
        True if the password is valid, False otherwise.
    """

    if len(password) < 8:
        return False
    
    U_count = 0
    for char in password:
        if char.isupper():
            U_count += 1
    if U_count < 1:
        return False
    
    D_count = 0
    for char in password:
        if char.isdigit():
            D_count += 1
    if D_count <= 1:
        return False
    
    special_chars = '!@#$%^&*()'
    s_count = 0
    for char in password:
        if char in special_chars:
            s_count += 1
    if s_count < 1:
        return False
    
    return True


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

    while True:
        mobile_no = input("enter mobile_no: ")
        logger = get_logger("validate_mobile_no")
        if validate_mobile_no(mobile_no):
            logger.info("mobile_no registered successfully")
            break
        else:
            logger.info("Invalid mobile_no. Please try again")

    while True:
        password = input("enter password: ")
        logger = get_logger("validate_password")
        if validate_password(password):
            logger.info("password registered successfully")
            break
        else:
            logger.info("Invalid password. Please try again")

    logger.info("User Registration successful!")


if __name__ == '__main__':
    main()

        
        
