"""
SDEV 300
Author: Charlemagne Marc
File: marc_charlemagne_lab3
Date: 01/31/2023
Lab Week 3
Purpose: Python program that allows a user to enter and validate their phone number and zipcode+4.
Then the user will enter values of two, 3x3 matrices and then select from options including,
addition, subtraction, matrix multiplication, and element by element multiplication.
"""
# imports
import re
import numpy as np


def print_greeting():
    """
    print_greeting(): prints greeting to user
    :return: None
    """
    # print greeting
    print("Greetings!\nThis python program allows a user to enter and validate their phone number"
          "and zipcode+4. Then the user will enter values of two, 3x3 matrices and then select from"
          "options including, addition, subtraction, matrix multiplication, and element by element"
          "multiplication.\n...")


def print_closing():
    """
    print_closing(): prints closing message
    :return: None
    """
    # print message
    print("...\nThanks for trying the Python Matrix Application.")


def print_dev_info(date):
    """
    print_dev_info(string): prints developer info
    :param date: string
    :return: None
    """
    # print message
    print(f"...\nDeveloper: Charlemagne Marc.\nClass: SDEV 300 7615.\n{date}")


def user_input(valid_responses):
    """
    user_input(tuple): returns a valid user input based upon tuple
    :param valid_responses: tuple
    :return: string
    """
    # get user input
    user_response = input().strip().upper()

    # if user input is in tuple return user input else print not valid and make a recursive call
    if user_response in valid_responses:
        return user_response

    print(f"Please, enter {valid_responses}:")
    return user_input(valid_responses)


def file_menu():
    """
    file_menu(): prints file menu
    :return: None
    """
    print("Select the file you want to analyze:\n1. Population Data\n2. Housing Data\n3. Exit the\
        Program")


def analysis_menu(column_tuple):
    """
    analysis_menu(): prints the population file menu
    :param column_tuple: tuple
    :return: None
    """
    # initilaize menu string
    menu = "Select the Column you want to analyze:"

    # start value of ascii value of a
    ascii_value = ord('a')

    # for loop to go through the strings in the column tuple
    for column in column_tuple:
        # add asii_value and column string to menu string
        menu += f"\n{chr(ascii_value)}. {column}"

        # increment ascii_value by one
        ascii_value += 1
    
    # add the exit column to menu string
    menu += f"\n{ascii_value} Exit Column"


def run_application():
    """
    print_menu(): print menu to console
    :return: None
    """
    # print menu
    file_menu()

    # get selection from user
    file_selection = user_input(('1', '2', '3'))

    # case statement
    match file_selection:
        # if 1 print You have entered Population Data. then run Population Data
        case '1':
            print("You have entered Population Data.")
        # if 2 then run Housing Data
        case '2':
            print("You have entered Housing Data.")
        # if 3 then return None
        case '3':
            print("You have entered Exit.")
            return None
    
    # recursive call to run application
    return run_application()


def main():
    """
    main(): main function
    :return: None
    """
    # print greeting
    print_greeting()

    # run application
    run_application()

    # print closing
    print_closing()

    # print dev info
    print_dev_info("02/07/2023")


if __name__ == "__main__":
    main()
