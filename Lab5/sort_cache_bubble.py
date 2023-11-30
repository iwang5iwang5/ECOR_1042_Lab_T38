# ECOR 1042 Lab 5 - Individual submission for sort_cache_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Stefan Martincevic"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295641"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-38"

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


# Do NOT include a main script in your submission
