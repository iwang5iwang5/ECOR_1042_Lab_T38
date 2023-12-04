# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Stefan Martincevic"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295641"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-38"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def histogram(dict_list: list, attribute: str) -> int:

    hist = {}

    hist_string = True

    for item in dict_list:

        hist_key = item[attribute]

        if hist_key in hist:
            hist[hist_key] += 1
        else:
            hist[hist_key] = 1

    keys = list(hist.keys())
    data = []

    if len(keys) > 0 and type(keys[0]) is int:
        hist_string = False
        keys.sort()

    for key in keys:
        data.append(hist[key])

    
    plt.bar(keys, data)

    # if hist_string == False:

    plt.set_ylabel('Count')
    plt.set_title('Histogram of ' + attribute)

    plt.show()

    if hist_string == True:
        return -1
    else:
        return keys[len(keys) - 1]

    # Do NOT include a main script in your submission
