# ECOR 1042 Lab 3 - Template

#I am writing stuff
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