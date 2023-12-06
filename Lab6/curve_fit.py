# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Esosa Ohangbon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297277"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
# Place your curve_fit function after this line
import matplotlib.pyplot as plt
import numpy as np


def curve_fit(dict_list: list, attribute: str, degree: int):
    x = []
    y = []
    for dictionary in dict_list:
        y += [dictionary["M_AVG"]]
        x += [dictionary[attribute]]
    if len(dict_list) < 5 and degree > len(dict_list) - 1:
        degree = len(dict_list) - 1
    line = np.polyfit(x, y, degree)

    equation = "y = "
    if degree == 0:
        equation += str(line[0])
    elif degree == 1:
        equation += str(line[0]) + "x + " + str(line[1])
    elif degree == 2:
        equation += str(line[0]) + "x^2 + " + \
            str(line[1]) + "x + " + str(line[2])
    elif degree == 3:
        equation += str(line[0]) + "x^3 + " + str(line[1]) + \
            "x^2 + " + str(line[2]) + "x + " + str(line[3])
    elif degree == 4:
        equation += str(line[0]) + "x^4 + " + str(line[1]) + "x^3 + " + \
            str(line[2]) + "x^2 + " + \
            str(line[3]) + "x + " + str(line[4])
    elif degree == 5:
        equation += str(line[0]) + "x^5 + " + str(line[1]) + "x^4 + " + str(line[2]) + \
            "x^3 + " + str(line[3]) + "x^2 + " + \
            str(line[4]) + "x + " + str(line[5])

    return equation

# Do NOT include a main script in your submission
