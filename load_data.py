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

    >>> machine_vendor_list(machine.csv, amdahl)
    [{'Model': '32/60', 'MYCT': '125', 'MMIN': '256', 'MMAX': '6000', 'CACH': '256', 'PRP': '198', 'ERP': '199'}]
    >>> machine_vendor_list(machine.csv, apollo)
    [{'Model': 'dn320', 'MYCT': '400', 'MMIN': '1000', 'MMAX': '3000', 'CACH': '0', 'PRP': '38', 'ERP': '23'}, {'Model': 'dn420', 'MYCT': '400', 'MMIN': '512', 'MMAX': '3500', 'CACH': '4', 'PRP': '40', 'ERP': '24'}]
    >>> machine_vendor_list(machine.csv, bti)
    [{'Model': '5000', 'MYCT': '350', 'MMIN': '64', 'MMAX': '64', 'CACH': '0', 'PRP': '10', 'ERP': '15'}, {'Model': '8000', 'MYCT': '200', 'MMIN': '512', 'MMAX': '16000', 'CACH': '0', 'PRP': '35', 'ERP': '64'}]
    """
    infile = open(filename, "r")
    header = infile.readline().strip().split(",")
    result = []
    for line in infile:
        line_lst = line.strip().split(",")
        if line_lst[0] == param:
            data = {}
            for i in range(1, len(header)):
                data[header[i]] = line_lst[i]

            result.append(data)
    infile.close()
    return result

    #Do not include a main script

#==========================================#
# Place your machine_model_list function after this line

# ECOR 1042 Lab 3 - Template


# Update 
__author__ = "Ivan Wang"
__student_number__ = "101298751"
__team__ = "T038"

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



#==========================================#
# Place your machine_prp_list function after this line



#==========================================#
# Place your load_data function after this line
def load_data(filename: str, filter: tuple) -> list[dict]:
    pass

#==========================================#
# Place your add_average_main_memory function after this line
def add_average_main_memory(machines: list[dict]) ->list[dict]:
    """Return list of machines with a new entry added to each dictionary.
    The new entry's key is 'M_AVG' with the value of the average of the memory usage.
    
    """
    for machine in machines:
        machine['M_AVG'] = (machine['MMAX'] + machine['MMIN']) / 2
    return machines
    


# Do NOT include a main script in your submission


