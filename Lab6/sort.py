# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Stefan Martincevic, Ivan Wang, Lance Downton, Esosa Ohangbon"

# Update "" with your team (e.g. T102)
__team__ = "T038"

#==========================================#
# Place your sort_cache_bubble function after this line
def sort_cache_bubble(dict_list: list, sorting_order: str) -> list:
    """
    Return a list of machines' dictionaries by the "CACH" attribute, using bubble sort, in either an ascending or descending order.

    Preconditions: None.

    >>> sort_cache_bubble([{'CACH': 12, 'Model': 'zt'}, {'CACH': 19, 'Model': 'MS'}, {'CACH': 10, 'Model': 'GP'}, {'CACH': 13, 'Model': 'PR'}], "A")
    [{'CACH': 10, 'Model': 'GP'}, {'CACH': 12, 'Model': 'zt'}, {'CACH': 13, 'Model': 'PR'}, {'CACH': 19, 'Model': 'MS'}]
    >>> sort_cache_bubble([{'CACH': 12, 'Model': 'zt'}, {'CACH': 19, 'Model': 'MS'}, {'CACH': 10, 'Model': 'GP'}, {'CACH': 13, 'Model': 'PR'}], "D")
    [{'CACH': 19, 'Model': 'MS'}, {'CACH': 13, 'Model': 'PR'}, {'CACH': 12, 'Model': 'zt'}, {'CACH': 10, 'Model': 'GP'}]
    >>> sort_cache_bubble([{"CACH":10,"Model":"GP"},{"CACH":19,"Model":"MS"}], "D")
    [{"CACH": 19, "Model":"MS"}, {"CACH":10, "Model":"GP"}]
    """

    for item in dict_list:
        if item.get("CACH") == None:
            print('"CACH" key is not present')
            return dict_list

    swap = True

    while swap:

        if sorting_order == 'A':

            swap = False

            for i in range(len(dict_list) - 1):
                if dict_list[i].get("CACH") > dict_list[i + 1].get("CACH"):
                    aux = dict_list[i]
                    dict_list[i] = dict_list[i + 1]
                    dict_list[i + 1] = aux
                    swap = True

        elif sorting_order == 'D':

            swap = False

            for i in range(len(dict_list) - 1):
                if dict_list[i].get("CACH") < dict_list[i + 1].get("CACH"):
                    aux = dict_list[i]
                    dict_list[i] = dict_list[i + 1]
                    dict_list[i + 1] = aux
                    swap = True

    return dict_list

#==========================================#
# Place your sort_prp_selection function after this line
def sort_prp_selection(machines: list[dict], order: str) -> list[dict]:
    """Return a list of dictionaries sorted by prp given a list of dictionaries and the order. 
    -If order is 'A', sort from least to greatest.
    -If order is 'D', sort from greatest to least.
    -If the dictionaries do not contain the key "PRP", the returns the original list and prints: '“PRP” key is
    not present.'

    Precondition: order == "A" or order == "D"

    >>> sort_prp_selection ( [{"PRP":10,"Model":"GP"}, {"PRP":19,"Model":"MS"}], "D")
    [{"PRP": 19, "Model":"MS"}, {"PRP":10, "Model":"GP"}]

    >>>sort_prp_selection([{"Model":"GP"},{"Model":"MS"}], "D")
    "PRP" key is not present
    [{"Model":"GP"}, {"Model":"MS"}]

    >>>sort_prp_selection([{'PRP': 2, 'Model': '2'}, {'PRP': 4, 'Model': '4'}, {'PRP': 1, 'Model': '1'}, {'PRP': 3, 'Model': '3'}], "A")
    [{'PRP': 1, 'Model': '1'}, {'PRP': 2, 'Model': '2'}, {'PRP': 3, 'Model': '3'}, {'PRP': 4, 'Model': '4'}]
    """

    #check if all machines contain "PRP" key
    if len(machines) > 0 and not "PRP" in machines[0]: #check if key is in each machine
        print('“PRP” key is not present.') #print if does not have "PRP"
        return machines #return original list
    
    if order == "A": #check sort order

        #selection sort least to greatest
        for i in range(len(machines)): #loop for each element
            smallest = i #create variable to hold index of smallest element and initialise to i
            for j in range(i+1, len(machines)): #loop for unsorted section
                if machines[smallest]["PRP"] > machines[j]["PRP"]:#check if "PRP" is smaller than current smallest
                    smallest = j #assign new smallest "PRP" index
            machines[i], machines[smallest] = machines[smallest], machines[i] #swap position


    elif order == "D": #check sort order

        #selection sort geatest to least
        for i in range(len(machines)):#loop for each element
            largest = i #create variable to hold index of biggest element and initialise to i
            for j in range(i+1, len(machines)): #loop for unsorted section
                if machines[largest]["PRP"] < machines[j]["PRP"]:#check if "PRP" is bigger than current biggest
                    largest = j #assign new biggest "PRP" index
            machines[i], machines[largest] = machines[largest], machines[i] #swap position
    
    #return list
    return machines

#==========================================#
# Place your sort_m_avg_insertion function after this line
def sort_m_avg_insertion(unsorted_list: list[dict], sorting_order: str) -> list[dict]:
    """
    Return a sorted list of dictionaries, were the dictionaries are sorted in ascending or descending
    order of their average main memory ("M_AVG"). However, if the key "M_AVG" is not found in the dictionaries
    within the unsorted list, then a message will be printed and the unsorted list will be returned.

    The first parameter, unsorted_list, takes a list of unsorted dictionaries.
    The second parameter, sorting_order, takes one of two strings ("A" or "D") to determine in what order list
    will be sorted:
        "A" - Sorts the list in ascending order
        "D" - Sorts the list in descending order

    >>>sort_m_avg_insertion([], "A")
    []

    >>>sort_m_avg_insertion([{"Model":"GP"}, {"Model":"MS"}], "D")
    [{"Model":"GP"}, {"Model":"MS"}]
    
    >>>sort_m_avg_insertion([{"M_AVG":7.2,"Model":"GP"}, {"M_AVG":9.1,"Model":"MS"}], "D")
    [{"M_AVG":9.1,"Model":"MS"}, {"M_AVG":7.2,"Model":"GP"}]
    """
    # Create copy of the unsorted list (unsure if we are suppose leave to original list alone)
    temp_list = unsorted_list

    # Verify that "M_AVG" exists and that the list is larger than one
    if len(temp_list) > 0 and temp_list[0].get("M_AVG", False):
    
        # Sort in ascending order
        if sorting_order == "A":
            
            # Iterate through every unsorted element
            for i in range(1, len(temp_list)):

                # Preparing to sort i into the sorted list
                dictionary = temp_list.pop(i)
                value = dictionary["M_AVG"]
                j = i - 1
            
                # Find where i goes in the sorted list
                while j >= 0 and value < temp_list[j]["M_AVG"]:
                    j -= 1

                # Insert i where it belongs in the sorted list
                temp_list.insert(j + 1, dictionary)

        # Sort in descending order
        elif sorting_order == "D":

            # Iterate through every unsorted element
            for i in range(1, len(temp_list)):

                # Preparing to sort i into the sorted list
                dictionary = temp_list.pop(i)
                value = dictionary["M_AVG"]
                j = i - 1
            
                # Find where i goes in the sorted list
                while j >= 0 and value > temp_list[j]["M_AVG"]:
                    j -= 1

                # Insert i where it belongs in the sorted list
                temp_list.insert(j + 1, dictionary)

    # If "M_AVG" does not exist, inform user
    elif len(temp_list) > 0:

        print('"M_AVG" key is not present')
    
    # Return sorted list or unsorted list depending on if "M_AVG" existed
    return temp_list

#==========================================#
# Place your sort_myct_bubble function after this line
def sort_myct_bubble(data: list[dict], order: str) -> list:
    """
    Return a sorted list of dictionaries by 'MYCT' attribute in either ascending 
    order or descending order depending on user input if the 'MYCT' key is 
    present in the dictionary, otherwise return the original list with a message
    "'MYCT' key is not present"

    Arguments:
    - data(list[dict]): List of dictionaries to be sorted.
    - order(str): Sorting order, 'A' for ascending, 'D' for descending.

    Examples:
    >>> sort_myct_bubble([{"MYCT":10,"Model":"GP"},{"MYCT":19,"Model":"MS"}],
        "D")
        [{"MYCT": 19, "Model":"MS"}, {"MYCT":10, "Model":"GP"}]
    >>> sort_myct_bubble([{"Model":"GP"}, {"Model":"MS"}], "D")
        "MYCT" key is not present.
        [{"Model":"GP"}, {"Model":"MS"}]
    """
    # Check if 'MYCT' is a key in the dictionary
    if len(data) > 0 and "MYCT" not in data[0]:
        print("'MYCT' key is not present.")
        return data

    # Loop to access each data element
    for i in range(len(data)):
        # Loop to compare data elements
        for j in range(0, len(data) - i - 1):

            # Ascending order
            if order == 'A':
                # Compare two adjacent elements
                if data[j]['MYCT'] > data[j + 1]['MYCT']:
                    # Swapping elements if elements are not in the intended order
                    data[j], data[j + 1] = data[j + 1], data[j]

            # Descending order
            elif order == 'D':
                # Compare two adjacent elements
                if data[j]['MYCT'] < data[j + 1]['MYCT']:
                    # Swapping elements if elements are not in the intended order
                    data[j], data[j + 1] = data[j + 1], data[j]

    return data

#==========================================#
# Place your sort function after this line
def sort(machines: list[dict], order: str, attribute: str):
    """Returns sorted list of dictionaries given the list of machines, the order,
    and attribute to sort by. It can sort by the attributes (“CACH”, “PRP”, “M_AVG”, “MYCT”)

    Precondition: order == "A" or "D" 

    >>>sort([{"Model":"GP"},{"Model":"MS"}], "D", "Model")
    Cannot be sorted by "Model"
    [{'Model': 'GP'}, {'Model': 'MS'}]

    >>>sort([{"CACH":10,"Model":"GP"},{"CACH":19.1,"Model":"MS"}], "D", "CACH")
    [{'CACH': 19.1, 'Model': 'MS'}, {'CACH': 10, 'Model': 'GP'}]

    >>>sort([{"CACH":5,"Model":"T"},{"CACH":2,"Model":"S"}], "A", "M_AVG")
    "M_AVG" key is not present
    [{'CACH': 5, 'Model': 'T'}, {'CACH': 2, 'Model': 's'}]
    """
    if attribute == "CACH":
        return sort_cache_bubble(machines, order)
    elif attribute == "PRP":
        return sort_prp_selection(machines, order)
    elif attribute == "M_AVG":
        return sort_m_avg_insertion(machines, order)
    elif attribute == "MYCT":
        return sort_myct_bubble(machines, order)
    else:
        print('Cannot be sorted by "' + attribute + '"')
        return machines
# Do NOT include a main script in your submission
