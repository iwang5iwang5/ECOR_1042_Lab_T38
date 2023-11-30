# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Lance Downton"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295784"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
# Place your script for your text_UI after this line

# Import load data and set it up for easier use later
import load_data
l_d = load_data.load_data
m_avg = load_data.add_average_main_memory

import sort

def get_command() -> None:
    """
    """
    # Set up
    exit_command = False
    data_loaded = False

    while not exit_command:

        # Inform user of available commands
        print("The available commands are:")
        #print('\033[1m' + "\tL)" + '\033[0m' + "oad Data") # Bolded L
        print("   L)oad Data") # Either 3 spaces or one \t not sure which looks better
        print("   S)ort Data")
        print("   C)urve Fit")
        print("   H)istogram")
        print("   E)xit", end="\n\n")

        # Get user command and insure it is lowercase
        command = input("Please type your command: ").lower()

        # Load data
        if command == "l":
            data_loaded = load_data_command()
        
        elif command == "s":
            sort_data()

        break

    print(data_loaded)


def load_data_command() -> list[dict]:
    """
    """
    # Promp user to get name of file to load
    filename = input("Please enter the name of the file: ")

    # Get filter
    while True:

        # Promp user for a filter
        attribute_filter = input("Please enter the attribute to use as a filter: ").lower()
        
        # Check if filter is valid and leave loop if it is
        if attribute_filter == "cach" or attribute_filter == "model" or attribute_filter == "prp" or attribute_filter == "vendor" or attribute_filter == "all":
            break
        
        # Inform user of an invaled filter inputed
        print("Invalid filter key.")
    
    # Get attribute value
    if attribute_filter == "model" or attribute_filter == "vendor":

        # Prompt user for attribute value
        attribute_value = input("Please enter the value of the attribute: ")

    elif attribute_filter != "all":

        # Prompt user for attribute value
        attribute_value = int(input("Please enter the value of the attribute: "))

    # Inform user that data was loaded and return the loaded data
    print("Data loaded")
    return m_avg(l_d(filename, (attribute_filter, attribute_value)))


def sort_data(data: list[dict]) -> None:
    """
    """


get_command()