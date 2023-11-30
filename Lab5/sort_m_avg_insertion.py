# ECOR 1042 Lab 5 - Individual submission for sort_m_avg_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Lance Downton"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295784"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

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

# Do NOT include a main script in your submission
