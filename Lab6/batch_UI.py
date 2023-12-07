# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ivan Wang"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298751"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
# Place your script for your batch_UI after this line
import curve_fit
import histogram
import load_data
import sort

#load data command
def load_data_command(e: list) -> list[dict]:
    """Return list of dictionaries of loaded data with average main memory given 
    a list of inputs (e) in the format [command, csv_file_name, filter_attribute, filter_value]
    filter_value is not included if filter_attribute is "ALL".

    Precondition: len(e) == 3 or 4

    >>>load_data_command(["L", "machine.csv", "vendor", "adviser"])
    data loaded
    [{'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}]

    >>>load_data_command(["L", "machine.csv", "all"])
    data loaded
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
        'CACH': 256, 'PRP': 198, 'ERP': 199},
      {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 269, 'ERP': 253}, 
      {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 220, 'ERP': 253}, 
      {another element},
      ...
    ]

    >>>load_data_command(["L", "machine.csv", "wrong thing", -20)
    Invalid Value
    []
    """
    #check if commands are valide
    if not e[2].lower() in ["vendor", "model","cach", "prp", "all"]:
        return []
    
    #check if it contains 4 elements
    if len(e) == 4:
        data = load_data.add_average_main_memory(load_data.load_data(e[1], (e[2],e[3]))) #load data with filter

    else:
        data = load_data.add_average_main_memory(load_data.load_data(e[1], (e[2],-1))) #load data without filter

    #check if data has been loaded
    if len(data) > 0:
        print("data loaded")
        return data
    
    #return loaded data
    return data

#call curve fit function
def curve_fit_command(e:list, data) -> str:
    """Return a str of the equation of best fit given e.
    """

    #check if there is data
    if data == []:
        print("File not loaded. Please, load a file first.")
        return #return nothing
    
    #call funtion
    return curve_fit.curve_fit(data,e[1],int(e[2]))

#call histogram function
def histogram_command(e:list , data:list[dict]) -> int:
    """Return an integer and displays a histogram given a list of instructions (e) and a list of data.
    """
    #check if there is data
    if data == []:
        print("File not loaded. Please, load a file first.")
        return #return nothing
    
    #call funtion
    return histogram.histogram(data,e[1])

#call sort funtion
def sort_command(e:list, data: list[dict]) -> list[dict]:
    """Return modified data list to be sorted given the sort instructions (e) and a list of data.

    Precondition: len(e) == 4, e = ["S", attribute, "A" or "D"]

    >>>sort_command(["S", "Model", "D"], [{"Model":"GP"},{"Model":"MS"}])
    Cannot be sorted by "Model"
    [{'Model': 'GP'}, {'Model': 'MS'}]

    >>>sort_command(["S", "CACH", "D"], [{"CACH":10,"Model":"GP"},{"CACH":19.1,"Model":"MS"}])
    [{'CACH': 19.1, 'Model': 'MS'}, {'CACH': 10, 'Model': 'GP'}]

    >>>sort_command(["S", "M_AVG", "A"], [{"CACH":5,"Model":"T"},{"CACH":2,"Model":"S"}])
    "M_AVG" key is not present
    [{'CACH': 5, 'Model': 'T'}, {'CACH': 2, 'Model': 's'}]
    """
    #check if there is data
    if data == []:
        print("File not loaded. Please, load a file first.")
        return []
    
    #sort data then return
    if e[3].lower() == "n":
        return sort.sort(data,e[2],e[1])
    
    #sort and display data, then return
    elif e[3].lower() == 'y':
        data = sort.sort(data,e[2],e[1])
        print(data)
        return data

#-------------------------------------------------------------------------------------------------
#start of main funtion
#-------------------------------------------------------------------------------------------------

def main_func() -> None:
    """Return nothing or None type. Prompts user for instruction file and exicute all instruction
    in instruction file.
    """

    #get filename
    filename = input("Please enter the name of the file where your commands are stored: ")

    #open file
    with open(filename, "r") as batch:

        #divide file by lines and put in array
        commands = batch.read().strip().split("\n")

        #divide each line into an array of commands
        for i in range(len(commands)):
            commands[i] = commands[i].strip().split(";")

        #create local varriable
        not_exit = True #instructed exit
        i = 0 #index of lines
        data = [] #data from file

        #loop through each line and exit after done or if instructed to
        while i < len(commands) and not_exit:

            #load data
            if commands[i][0].upper() == "L":
                data = load_data_command(commands[i])

            #sort
            elif commands[i][0].upper() == "S":
                data = sort_command(commands[i], data)

            #curve fit
            elif commands[i][0].upper() == "C":
                print(curve_fit_command(commands[i], data))
            
            #histogram
            elif commands[i][0].upper() == "H":
                histogram_command(commands[i], data)

            #exit
            elif commands[i][0].upper() == "E":
                not_exit = False

            #invalid commands
            else:
                print("Invalid command.")
            
            #move to next line
            i += 1
        
        #print all data
        print(data)
main_func()