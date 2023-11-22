# ECOR 1042 Lab 3 - Template


# Update "" to list all students contributing to the team work
__author__ = "Stefan Martincevic, Ivan Wang, Lance Downton, Esosa Ohangbon"

# Update "" with your team (e.g. T102)
__team__ = "T38"
 
#==========================================#
# Place your machine_vendor_list function after this line
def machine_vendor_list(filename: str, param: str) -> list[dict]:
    """
    Return a list of machines that belong to a specifc vendor. Return an empty list if the vendor does not exist.

    Preconditions: None

    >>> machine_vendor_list(machine.csv, adviser)
    [{'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}]
    >>> machine_vendor_list(machine.csv, apollo)
    [{'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}, {'Model': 'dn420', 'MYCT': 400, 'MMIN': 512, 'MMAX': 3500, 'CACH': 4, 'PRP': 40, 'ERP': 24}]
    >>> machine_vendor_list(machine.csv, bti)
    [{'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15}, {'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64}]
    """
    # Open and read file
    infile = open(filename, "r")
    
    # Remove whitespace from elements of the header and splits them into list
    header = infile.readline().strip().split(",")
    
    # Initialize list that contains all information about the machines of a vendor
    result = []
    
    # Loop that iterates for every line in the file
    for line in infile:
        
        # Remove whitespace from elemenst of the specific machine and splits them into list
        line_lst = line.strip().split(",")
        
        # Checks to see if the vendor is the vendor entered
        if line_lst[0] == param:
            
            # Initializing an empty dictionary for the vendor's information on a specific line
            data = {}
            
            # Loop that iterates for the amount of headers
            for i in range(1, len(header)):
                try:
                    # Attempt to change machine information to integer
                    data[header[i]] = int(line_lst[i])
                except:
                    # If not, return to default of string
                    data[header[i]] = line_lst[i]

            # Add the information of the line to teh result
            result.append(data)
    # Close file
    infile.close()
    
    # Return result
    return result


#Do not include a main script

#==========================================#
# Place your machine_model_list function after this line
def machine_model_list(file_name: str, model: str) -> list[dict]:
    """Return list of machine dictionaries of the specified model. The dictionaries 
    contain all given information execpt the model with the header as the key given 
    the file_name containing the path to a csv file and the model.
    
    Preconditions: len(file_name) > 0, len(model) > 0

    >>>machine_model_list("machine.csv", '32/60')
    [{'Vendor': 'adviser', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}]
    >>>machine_model_list("machine.csv", 'non existent model')
    []
    >>>machine_model_list("machine.csv", 'dn420')
    [{'Vendor': 'apollo', 'MYCT': 400, 'MMIN': 512, 'MMAX': 3500, 'CACH': 4, 'PRP': 40, 'ERP': 24}]
    """
    #create list
    machine_list = []
    
    #open file
    with open(file_name, "r") as file:
        
        #get the header
        headers = file.readline().split(",")

        #remove white space from header and check for model
        for i in range(len(headers)):
            headers[i] = headers[i].strip()

        #read the first line
        line = file.readline()
        
        #loop for each line of the file.
        while line != '':
        
            #make sure line is not empty
            if line != '\n':
                
                #split line
                line = line.split(",")

                #create temperary dictionary
                temp_dict = {}

                #check if the model are the same as the specified model
                if model == line[1]:

                    #loop for each header
                    for i in range(len(headers)):

                        #remove white space
                        line[i] = line[i].strip()
                        
                        #make sure
                        if i != 1:

                            try:#try to int casting the line
                                temp_dict[headers[i]] = int(line[i])
                            except:#if not store value as str
                                temp_dict[headers[i]] = line[i]

                    #add new dictionary to list
                    machine_list += [temp_dict]

            #read next line
            line = file.readline()
            
    #return
    return machine_list

#Do not include a main script

#==========================================#
# Place your machine_cache_list function after this line

def machine_cache_list(filename: str, min_cache: int) -> list[dict]:
    """Return a list containing dictionaries with the information of the machines
    that have at least the minimum cache memory (in kilobytes) specified. However, if no machine
    is found to meet this requirement, then the list returned will be empty.

    Precondition: min_cache >= 0
    
    Assume machine.csv contains:

    Vendor,Model,MYCT,MMIN,MMAX,CACH,PRP,ERP
    adviser,32/60,125,256,6000,256,198,199
    amdahl,470v/7,29,8000,32000,32,269,253
    amdahl,470v/7a,29,8000,32000,32,220,253
    amdahl,470v/7b,29,8000,32000,32,172,253
    amdahl,470v/7c,29,8000,16000,32,132,132
    amdahl,470v/b,26,8000,32000,64,318,290
    amdahl,580-5840,23,16000,32000,64,367,381
    ...

    >>>machine_cache_list("machine.csv", 128)
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'PRP': 198, 'ERP': 199},
    {'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238},
    {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124},
    {'Vendor': 'cdc', 'Model': 'cyber:170/750', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 274, 'ERP': 102},
    {'Vendor': 'cdc', 'Model': 'cyber:170/760', 'MYCT': 25, 'MMIN': 1310, 'MMAX': 2620, 'PRP': 368, 'ERP': 102},
    {'Vendor': 'gould', 'Model': 'concept:32/8780', 'MYCT': 75, 'MMIN': 2000, 'MMAX': 16000, 'PRP': 259, 'ERP': 157},
    {'Vendor': 'nas', 'Model': 'as/9000-dpc', 'MYCT': 38, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 426},
    {'Vendor': 'nas', 'Model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 603},
    {'Vendor': 'ncr', 'Model': 'v8665', 'MYCT': 38, 'MMIN': 8000, 'MMAX': 24000, 'PRP': 140, 'ERP': 281},
    {'Vendor': 'ncr', 'Model': 'v8670', 'MYCT': 38, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 212, 'ERP': 190},
    {'Vendor': 'siemens', 'Model': '7.881-2', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 405, 'ERP': 382},
    {'Vendor': 'sperry', 'Model': '1100/94', 'MYCT': 30, 'MMIN': 8000, 'MMAX': 64000, 'PRP': 1150, 'ERP': 978}]

    >>>machine_cache_list("machine.csv", 200)
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'PRP': 198, 'ERP': 199},
    {'Vendor': 'nas', 'Model': 'as/9060', 'MYCT': 30, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 510, 'ERP': 603}]

    >>>machine_cache_list("machine.csv", 300)
    []
    """
    #Store information of found machines
    machine_information = []

    #Open and read the file with the given filename
    with open(filename, "r") as file:

        #Get a list of the headers in the file
        line = file.readline()
        headers = line.strip().split(",")

        #Read the rest of the file
        reading = True
        while reading:

            #Read next line
            line = file.readline()

            #If there is no more lines, it is the end of the file
            if not line:

                #Stop reading
                reading = False

            else:

                #Get machine's cache memory and convert it to an interger
                values = line.strip().split(",")
                cache = int(values[5])

                #If the machine has at least the minimum cache memory, store it
                if cache >= min_cache:
                    
                    #Dictionary to store machine information
                    information = {}

                    #Iterate through every attribute
                    for i in range(len(headers)):

                        #If the attribute is not cach memory save the information
                        if headers[i] != 'CACH':

                            #Try to convert the value to an integer
                            try:

                                value = int(values[i])

                            except:

                                value = values[i]

                            #Add the information to the dictionary
                            information[headers[i]] = value
                        
                    #Add the machines information to "machine_information"
                    machine_information += [information]

    #Return the list with all dictionaries containing the machine information
    return machine_information

#==========================================#
# Place your machine_prp_list function after this line
def machine_prp_list(file_name, min_performance):
    """
    Return a list of dictionaries, each representing a machine with attributes meeting the minimum performance provided by the user.

    Arguments:
    - file_name (str): The name of the file containing machine data in CSV format.
    - min_performance (int): The minimum acceptable published relative performance.

    Examples:
    >>> machine_prp_list('machine.csv', 150)
    [   {'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256,
        'MMAX': 6000, 'CACH': 256, 'ERP':199},
        {another element},
        …
    ]
    >>> machine_prp_list('machine.csv', 1500)
        []

    """

    machines = []

    # Read data from the CSV file
    with open(file_name, 'r') as file:
        line = file.readline()
        headers = line.strip().split(',')

        for lines in file:
            # Convert 'PRP' to integer for comparison
            values = lines.strip().split(',')
            machine = {}
            if int(values[6]) >= min_performance:
                for i in range(len(headers)):
                    if headers[i] != 'PRP':
                        try:
                            value = int(values[i])
                        except:
                            value = values[i]
                        machine[headers[i]] = value
                machines += [machine]

    return machines



#==========================================#
# Place your load_data function after this line
def load_data(filename: str, filter: tuple) -> list[dict]:
    """Returns list of dictionaries contain each machine that fits the filter given
    the filename str that contains all the machines and a tuple. The first element of the
    tuple is a str contain what element is being filtered like "vendor", "model","cach", "prp",
    or "all". "all" will return a list containing the dictionaries of all the machines without 
    excluding any colums. If the filter is unknown, then it will print "Invalid Value" and return
    an empty list. The second contains the filter condition.

    Precondition: len(filename) > 0, len(filter) == 2, type(filter[0]) == <class 'str'>

    >>>load_data("machine.csv", ("vendor", "adviser"))
    [{'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}]

    >>>load_data("machine.csv", ("all", -20))
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
        'CACH': 256, 'PRP': 198, 'ERP': 199},
      {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 269, 'ERP': 253}, 
      {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 220, 'ERP': 253}, 
      {another element},
      ...
    ]

    >>>load_data("machine.csv", ("wrong thing", -20))
    Invalid Value
    []
    """
    action = filter[0]
    requirement = filter[1]
    information = []

    if action.lower() == "all":

        with open(filename, 'r') as file:

            first_line = file.readline()
            headers = first_line.strip().split(',')

            for line in file:

                data = {}
                values = line.strip().split(',')

                for i in range(len(headers)):

                    try:

                        value = int(values[i])

                    except:

                        value = values[i]

                    data[headers[i]] = value
                
                information += [data]

    elif action.lower() == "vendor":

        information = machine_vendor_list(filename, requirement)

    elif action.lower() == "model":

        information = machine_model_list(filename, requirement)

    elif action.lower() == "cach":

        information = machine_cache_list(filename, requirement)

    elif action.lower() == "prp":

        information = machine_prp_list(filename, requirement)

    else:

        print("Invalid Value")
    
    return information

#==========================================#
# Place your add_average_main_memory function after this line
def add_average_main_memory(machines: list[dict]) -> list[dict]:
    """Return list of machines with a new entry added to each dictionary.
    The new entry's key is 'M_AVG' with the value of the average of the memory usage.

    Preconditions: machines[i] contains machines[i]['MMax'] and machines[i]['MMin']
    
    >>>add_average_main_memory([{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
        'CACH': 256, 'PRP': 198, 'ERP': 199}])
    
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
    'CACH': 256, 'PRP': 198, 'ERP': 199, 'M_AVG': 3128.0}]

    >>>add_average_main_memory([])
    []

    >>>add_average_main_memory([{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
        'CACH': 256, 'PRP': 198, 'ERP': 199},
      {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 269, 'ERP': 253}, 
      {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 220, 'ERP': 253}
    ])

    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
        'CACH': 256, 'PRP': 198, 'ERP': 199, 'M_AVG': 3128.0}, 
      {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 269, 'ERP': 253, 'M_AVG': 20000.0}, 
      {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
      'CACH': 32, 'PRP': 220, 'ERP': 253, 'M_AVG': 20000.0}]

    """
    for machine in machines:
        machine['M_AVG'] = (machine['MMAX'] + machine['MMIN']) / 2
    return machines
    


# Do NOT include a main script in your submission
