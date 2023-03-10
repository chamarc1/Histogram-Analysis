"""
SDEV 300
Author: Charlemagne Marc
File: marc_charlemagne_lab5
Date: 01/31/2023
Lab Week 5
Purpose: Python program that allows a user to load one of two CSV files and then perform histogram
analysis and plots for select variables on the datasets. The first dataset represents the
population change for specific dates for U.S. regions. The second dataset represents Housing data
over an extended period of time describing home age, number of bedrooms and other variables.
"""
# imports
import csv
import numpy as np
import matplotlib.pyplot as plt


def print_greeting():
    """
    print_greeting(): prints greeting to user
    :return: None
    """
    # print greeting
    print("Greetings!\nThis python program allows a user to load one of two CSV files and then "\
        "perform histogram analysis and plots for select variables on the datasets.\n")

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
    print("Select the file you want to analyze:\n1. Population Data\n2. Housing Data\n3. Exit the"\
        " Program\n")


def analysis_menu(column_tuple):
    """
    analysis_menu(): prints the population file menu
    :param column_tuple: tuple
    :return letter_dictionary: dictionary
    """
    # initilaize menu string
    menu = "Select the Column you want to analyze:"

    # start value of ascii value of a
    ascii_value = ord('a')

    # create dictionary letter=key column_name=value
    letter_dictionary = {}

    # for loop to go through the strings in the column tuple
    for column in column_tuple:
        # add asii_value and column string to menu string
        menu += f"\n{chr(ascii_value)}. {column}"

        # add new key/value pair to dictionary
        letter_dictionary[str(chr(ascii_value)).upper()] = column

        # increment ascii_value by one
        ascii_value += 1

    # add the exit column to menu string and dictionary
    menu += f"\n{chr(ascii_value)} Exit Column"
    letter_dictionary[str(chr(ascii_value)).upper()] = None

    # print menu
    print(f"{menu}\n")

    # return dictionary
    return letter_dictionary


def get_column(file_name, column_name):
    """
    get_column(file_name, column_name): accesses the file by the file name given, then
        populates a np array of values in the column given to be returned
    :param file_name: string
    :param column_name: string
    :return: numpy array
    """
    # initialize numpy array
    column_array = np.array([])

    # open csv file
    with open(file_name, 'r', encoding="utf-8") as file:
        # create csv object
        reader = csv.reader(file)

        # find the index of column_name
        header = next(reader)
        column_index = header.index(column_name)

        for row in reader:
            # append value to np array
            column_array = np.append(column_array, float(row[column_index]))

    # return column array
    return column_array


def get_dictionary(file_name, column_name_tuple):
    """
    get_dictionary(file_name, column_name_tuple): creates dictionary of column names as keys and
        column data arryays as values
    :param file_name: name of csv file
    :param column_name_tuple: tuple of column names
    """
    # initialize dictionary
    data_dict = {}

    # for loop to iterate through tuple
    for column_name in column_name_tuple:
        # add to dictionary key=column_name value=get_column
        data_dict[column_name] = get_column(file_name, column_name)

    # return dictionary
    return data_dict


def display_histogram(data_array):
    """
    display_histogram(data_array): display histogram basaed on array
    :return: none
    """
    plt.hist(data_array)
    plt.show()


def calculate_statistics(data_dict, column_name_tuple):
    """
    calculate_statistics(data_dict, column_name_tuple): calculate statistics based on column
    :param data_dict: dictionary of data
    :column_name_tuple: tuple of column names
    :return: None or recursive call
    """
    # print the analyze menu
    letter_dictionary = analysis_menu(column_name_tuple)

    # get selection from user
    column_selection = user_input(tuple(letter_dictionary.keys()))

    # if selection=none return none
    if letter_dictionary[column_selection] is None:
        return None

    # get array based on selection
    data_array = data_dict[letter_dictionary[column_selection]]

    # calculate and print count
    count = data_array.size

    # calculate mean
    mean = np.mean(data_array)

    # calculate Standard Deviation
    std_deviation = np.std(data_array)

    # calculate Min
    min_value = np.min(data_array)

    # calculate and Max
    max_value = np.max(data_array)

    # print statistics
    print(f"You selected {letter_dictionary[column_selection]}\nThe statistics for this "\
        f"column are:\nCount = {count}\nMean = {mean}\nStandard Deviation = {std_deviation}\n"\
            f"Min = {min_value}\nMax = {max_value}\nThe Histogram is now displayed.")

    # display histogram
    display_histogram(data_array)

    # recursive call
    return calculate_statistics(data_dict, column_name_tuple)


def analyze_data(file_name, column_name_tuple):
    """
    analyze_data(filen_name, column_name_tuple): function that creates dictionaries based on given
        file. Then analyzes data based on user prompt
    """
    # get dictionary
    data_dict = get_dictionary(file_name, column_name_tuple)

    # calculate statistics
    calculate_statistics(data_dict, column_name_tuple)


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
            analyze_data("PopChange.csv", ("Pop Apr 1", "Pop Jul 1", "Change Pop"))
        # if 2 then run Housing Data
        case '2':
            print("You have entered Housing Data.")
            analyze_data("Housing.csv", ("AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"))
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
