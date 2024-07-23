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


def main():

    while True:
        first_name = input("Enter a valid first name: ")
        logger = get_logger("validate_first_name")
        if validate_first_name(first_name):
            logger.info("first_name registered successfully")
            break
        else:
            logger.info("Invalid first name. Please try again.")


if __name__ == '__main__':
    main()

        
        
