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

# importing libraries
import matplotlib.pyplot as plt
import numpy as np


def histogram(dict_list: list, attribute: str) -> int:
    """
    Return -1 if attribute is categroical and the maximum value if the attribute is numerical, as well as create a histogram. The function will take an input string of a list of dictionaries and a string that indicates an attribute.

    Preconditions: None.

    >>> histogram([{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000,
              'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132},
             {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000,
                 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238},
             {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400,
                 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23},
             {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000,
                 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70},
             {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000,
                 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117},
             {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64,
                 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15},
             {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512,
                 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64},
             {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167,
                 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23},
             {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143,
                 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29},
             {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143,
                 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22},
             {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110,
                 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124},
             {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143,
                 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35},
             {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143,
                 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39},
             {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143,
                 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40},
             {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 3110,
                 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}], 'CACH')
    142
    >>> histogram([{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000,
              'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132},
             {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000,
                 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238},
             {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400,
                 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23},
             {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000,
                 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70},
             {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000,
                 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117},
             {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64,
                 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15},
             {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512,
                 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64},
             {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167,
                 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23},
             {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143,
                 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29},
             {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143,
                 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22},
             {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110,
                 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124},
             {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143,
                 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35},
             {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143,
                 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39},
             {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143,
                 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40},
             {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 3110,
                 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}], 'Vendor')
    -1
    >>> histogram([{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000,
              'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253},
             {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000,
                 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132},
             {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000,
                 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23,
                 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749},
             {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000,
                 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238},
             {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400,
                 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23},
             {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000,
                 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70},
             {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000,
                 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117},
             {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64,
                 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15},
             {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512,
                 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64},
             {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167,
                 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23},
             {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143,
                 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29},
             {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143,
                 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22},
             {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110,
                 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124},
             {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143,
                 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35},
             {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143,
                 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39},
             {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143,
                 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40},
             {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 3110,
                 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}], 'Model')
    -1
    """

    # Initializing histogram dictionary
    hist = {}

    # initializing return result to -1
    result = -1

    # Iterating thorugh input list of dictionaries
    for item in dict_list:

        # Finding histogram key of the specific attribute
        hist_key = item[attribute]

        # Checking to see if histogram key is already in the histogram
        if hist_key in hist:

            # Increment count for key it is in the histogram
            hist[hist_key] += 1
        else:
            # Add key to the histogram
            hist[hist_key] = 1

    # Get list of keys
    keys = list(hist.keys())

    # Initialize data for plotting in a list
    data = []

    # setup plot title and y axis title
    plt.ylabel('Count')
    plt.title('Histogram of ' + attribute)

    # Checking to see if the key exists and if they are integers
    if len(keys) > 0 and type(keys[0]) is int:

        # Sort histogram bins in ascending order
        keys.sort()
        # Assigning return result to the last/largest key
        result = keys[len(keys) - 1]

        # Generate 20 intervals for the bins in the histogram x axis
        plt.xticks(np.arange(0, result + 1, result / 20))

    # Iterates over all keys
    for key in keys:
        # Fill up data list for the histogram
        data.append(hist[key])

    # Plot data
    plt.bar(keys, data)

    # Return result
    return result

    # Do NOT include a main script in your submission
