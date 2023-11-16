# ECOR 1042 Lab 3 - Template


# Update 
__author__ = "Lance Downton"
__student_number__ = "101295784"
__team__ = "038"

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
                    for i in range(len(values)):

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


#Do not include a main script

