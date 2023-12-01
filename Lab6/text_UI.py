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
data_loader = load_data.load_data
m_avg = load_data.add_average_main_memory

# Import sort and set it up for easier use later
import sort
data_sorter = sort.sort

def get_command() -> None:
    """
    """
    # Set up
    exit_command = False
    data_loaded = False
    loaded_type = ""

    # Iterate until user prompts to exit program
    while not exit_command:

        # Inform user of available commands
        print("The available commands are:")
        print("   L)oad Data") # Either 3 spaces or one \t not sure which looks better
        print("   S)ort Data")
        print("   C)urve Fit")
        print("   H)istogram")
        print("   E)xit", end="\n\n")

        # Get user command
        command = input("Please type your command: ").lower()

        # Load data
        if command == "l":
            data_loaded, loaded_type = load_data_command()
        
        # Sort data
        elif command == "s" and data_loaded:
            data_loaded = sort_data(data_loaded, loaded_type)

        # Curve fit data
        elif command == "c" and data_loaded:
            curve_fit_data(data_loaded, loaded_type)

        # Make histogram with data
        elif command == "h" and data_loaded:
            histogram_of_data(data_loaded, loaded_type)

        # Exit program
        elif command == "e" and data_loaded:
            exit_command = True

        # Try to manipulate data without loading any
        elif not data_loaded and (command == "l" or command == "s" or command == "c" or command == "h"):
            print("File not loaded. Please, load a file first.")

        # Invalid command
        else:
            print("Invalid command")


def load_data_command() -> (list[dict], str):
    """
    """
    # Prompt user to get name of file to load
    filename = input("Please enter the name of the file: ")

    # Get filter
    valid_filter = False
    while not valid_filter:

        # Prompt user for a filter
        attribute_filter = input("Please enter the attribute to use as a filter: ").upper()
        
        # Check if filter is valid and leave loop if it is
        if attribute_filter == "CACH" or attribute_filter == "MODEL" or attribute_filter == "PRP" or attribute_filter == "VENDOR" or attribute_filter == "ALL":
            valid_filter = True
        
        # Inform user of an invaled filter inputed
        else: 
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
    return (m_avg(data_loader(filename, (attribute_filter, attribute_value))), attribute_filter)


def sort_data(data: list[dict], loaded_type: str) -> list[dict]:
    """
    """
    # Get attribute to sort by
    valid_attribute = False
    while not valid_attribute:

        # Prompt user for an attribute
        sorting_attribute = input("Please enter the attribute you want to use for sorting:\n'CACH', 'PRP', 'M_AVG', 'MYCT':\n").upper()

        # Check if input is a valid attribute and present
        if sorting_attribute != loaded_type and (sorting_attribute == "CACH" or sorting_attribute == "PRP" or sorting_attribute == "M_AVG" or sorting_attribute == "MYCT"):
            valid_attribute = True
        
        # Attribute is not present
        elif sorting_attribute == loaded_type:
            print("Attribute {} is not present.".format(loaded_type))

        # Inform user of an invaled value attribute
        else:
            print("Invalid attribute.")
        
    # Get the order to sort
    valid_order = False
    while not valid_order:

        # Prompt user for sorting order
        sorting_order = input("Ascending (A) or Descending (D) order: ").upper()

        # Check if input is a valid order
        if sorting_order == "A" or sorting_order == "D":
            valid_order = True
        
        # Inform user of an invaled order
        else:
            print("Invalid order.")
        
    # Sort the loaded data
    sorted_data = data_sorter(data, sorting_order, sorting_attribute)

    # Prompt user on if they want to have sorted data displayed
    display_data = input("Data Sorted. Do you want to display the data?: ").lower()

    # Display data
    if display_data == "y":
        print(sorted_data)
    
    # Return sorted data
    return sorted_data


def curve_fit_data(data: list[dict], loaded_type: str) -> None:
    """
    """
    pass


def histogram_of_data(data: list[dict], loaded_type: str) -> None:
    """
    """
    pass

get_command()