# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Lance Downton"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295784"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
# Place your script for your text_UI after this line

def get_command():
    """
    """
    # Set up
    valid_commands = {"l", "s", "c", "h", "e"}
    valid_command = False
    data_loaded = False

    while not valid_command:

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

        # Check if inputted command is valid
        if command not in valid_commands:
            print("Invalid command.")
            continue
        
        # Load data
        elif command == "l":
            

        break

def load_data_command():
    """
    """
    # Get name of file to load
    filename = input("Please enter the name of the file: ").lower()

    # Get filter
    valid_filters = {"all", "model", "vendor", "prp", "cach"}
    attribute_filter = ""

    # Wait for filter to be valid
    while attribute_filter not in valid_filters:



get_command()