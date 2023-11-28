# ECOR 1042 Lab 5 - Individual submission for sort_prp_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ivan Wang"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298751"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

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
    for machine in machines:
        if not "PRP" in machine: #check if key is in each machine
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


# Do NOT include a main script in your submission