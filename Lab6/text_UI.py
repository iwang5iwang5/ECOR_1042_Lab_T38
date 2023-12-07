# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Lance Downton"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295784"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
# Place your script for your text_UI after this line

"""Examples on using the functions in this module can be found in the video demestration."""

# Import load data and set it up for easier use later
import load_data
data_loader = load_data.load_data
m_avg = load_data.add_average_main_memory

# Import the sort function from the sort file
from sort import sort

# Import the histogram function from the histogram file
from histogram import histogram

# Import the curve_fit function from the curve_fit file
from curve_fit import curve_fit

def get_command() -> list[dict]:
    """Prompts the user for input on what command they would like to run.
    These commands allow the user to:
        - Load data from a csv file, the input for this command is "L"
        - Sort the loaded data, the input for this command is "S"
        - Get a polynomial equation from the loaded data, the input for this command is "C"
        - Display a histogram using the loaded data, the input for this command is "H"
        - Exit the program, the input for this command is "E"
    """
    # Set up
    exit_command = False
    data_loaded = False
    loaded_type = ""

    # Iterate until user prompts to exit program
    while not exit_command:

        # Inform user of available commands
        print("The available commands are:")
        print("   L)oad Data")
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
            data_loaded = sort_data_command(data_loaded, loaded_type)

        # Curve fit data
        elif command == "c" and data_loaded:
            curve_fit_data_command(data_loaded, loaded_type)

        # Make histogram with data
        elif command == "h" and data_loaded:
            histogram_of_data_command(data_loaded, loaded_type)

        # Exit program
        elif command == "e":
            exit_command = True

        # Try to manipulate data without loading any
        elif not data_loaded and (command == "l" or command == "s" or command == "c" or command == "h"):
            print("File not loaded. Please, load a file first.")

        # Invalid command before data loaded
        elif not data_loaded:
            print("No such command")

        # Invalid command
        else:
            print("Invalid command")

    return data_loaded


def load_data_command() -> (list[dict], str):
    """Return a tuple containing two elements. The first element is
    the list loaded by the function load_data. The second element is
    the attribute that was used to load the data.

    The user is prompted to input the arguments to be passed to the load_data function.
    These arguments are the following:
        - Attribute to use as a filter when loading the data
        - The value of the filter used to load the data
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
        
        # Inform user of an invalid filter inputed
        else: 
            print("Invalid filter key.")
    
    # Get attribute value
    if attribute_filter == "MODEL" or attribute_filter == "VENDOR":

        # Prompt user for attribute value
        attribute_value = input("Please enter the value of the attribute: ")

    elif attribute_filter != "ALL":

        # Prompt user for attribute value
        attribute_value = int(input("Please enter the value of the attribute: "))

    # Give the attribute value a placeholder value
    elif attribute_filter == "ALL":
        attribute_value = "If you see this you are super cool :D"

    # Inform user that data was loaded and return the loaded data
    print("Data loaded")
    return (m_avg(data_loader(filename, (attribute_filter, attribute_value))), attribute_filter)


def sort_data_command(data: list[dict], loaded_type: str) -> list[dict]:
    """Return a sorted copy of the list that was passed as the argument.

    The user is prompted to input the arguments to be passed to the sort function.
    These arguments are the following:
        - Attribute for which the list will be sorted by
        - The order that the list will be sorted in (Ascending or Descending)
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
            print("Attribute {} is not present in the loaded data.".format(loaded_type))

        # Inform user of an invalid attribute
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
        
        # Inform user of an invalid order
        else:
            print("Invalid order.")
        
    # Sort the loaded data
    sorted_data = sort(data, sorting_order, sorting_attribute)

    # Prompt user on if they want to have sorted data displayed
    display_data = input("Data Sorted. Do you want to display the data?: ").lower()

    # Display data
    if display_data == "y":
        print(sorted_data)
    
    # Return sorted data
    return sorted_data


def curve_fit_data_command(data: list[dict], loaded_type: str) -> None:
    """Display the best fitting polynomial equation for M_AVG compared to
    a different attribute.

    The user is prompted to input the arguments to be passed to the curve_fit function.
    These arguments are the following:
        - The attribute to compare M_AVG to
        - The order of the fitted polynomial
    """
    # Get attribute to comapare M_AVG to
    valid_attribute = False
    while not valid_attribute:
        
        # Prompt user for an attribute
        fit_attribute = input("Please enter the attribute you want to use to find the best fit for M_AVG: ").upper()

        # Check if input is a valid attribute
        if fit_attribute != loaded_type and (fit_attribute == "MYCT" or fit_attribute == "MMIN" or fit_attribute == "MMAX" or fit_attribute == "CACH" or fit_attribute == "PRP" or fit_attribute == "ERP" or fit_attribute == "M_AVG"):
            valid_attribute = True

        # Inform user of an invalid attribute
        else:
            print("Invalid attribute.")

    # Get the order to fit the curve to
    valid_order = False
    while not valid_order:

        # Prompt user for the order
        fit_order = input("Please enter the order of the polynomial to be fitted: ")

        # Check if user input can be converted to an integer
        try:
            fit_order = int(fit_order)

            # Insure that the order is a valid order for the data loaded
            if fit_order < len(data) and fit_order > 0:
                valid_order = True

            # Inform user of an invalid order
            else:
                print("Invalid order.")

        # Inform user of an invalid order
        except:
            print("Invalid order.")

    # Get and print the polynomial equation
    fitted_curve = curve_fit(data, fit_attribute, fit_order)
    print(fitted_curve)
        

def histogram_of_data_command(data: list[dict], loaded_type: str) -> None:
    """Display a histogram of the values of a attributes.

    The user is prompted to input the arguments to be passed to the histogram function.
    These arguments are the following:
        - The attribute to use for the histogram's values
    """
    # Get attribute for the histogram
    valid_attribute = False
    while not valid_attribute:

        # Prompt user for an attribute
        histogram_attribute = input("Please enter the attribute you want to use for plotting: ").upper()

        # Check if input is a valid attribute
        if loaded_type != histogram_attribute and (histogram_attribute == "MODEL" or histogram_attribute == "VENDOR" or histogram_attribute == "MYCT" or histogram_attribute == "MMIN" or histogram_attribute == "MMAX" or histogram_attribute == "CACH" or histogram_attribute == "PRP" or histogram_attribute == "ERP" or histogram_attribute == "M_AVG"):
            valid_attribute = True

            # Vendor is fixed to be what the function expects
            if histogram_attribute == "VENDOR":
                histogram_attribute = "Vendor"
        
            # Model is fixed to be what the function expects
            elif histogram_attribute == "MODEL":
                histogram_attribute = "Model"

        # Inform user of an invalid attribute
        else:
            print("Invalid attribute.")
            
    # Get and display the histogram
    histogram(data, histogram_attribute)

#-------------------------------------------------------------------------------------------------
#start of main funtion
#-------------------------------------------------------------------------------------------------

# Start the UI, to start prompting the user
get_command()