# ECOR 1042 Lab 5 - Individual submission for sort_myct_bubble function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Esosa Ohangbon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297277"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

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


# Do NOT include a main script in your submission
