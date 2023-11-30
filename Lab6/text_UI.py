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

        # Load data
        if command == "l":
            load_data_command()

        break

def load_data_command():
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
    if attribute_filter != "all":

        # Prompt user for attribute value


get_command()