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
import numpy as np

def curve_fit(dict_list: list, attribute: str, degree: int):
    """
    Return the equation of a curve that best fits when given a data set.
    
    Parameters:
    - dict_list(list): A list of dictionaries representing data points. Each dictionary
    contains keys for 'M_AVG' (dependent variable) and the specified attribute.
    - attribute(str): The attribute within the dictionaries to be used as the independent variable.
    - degree(int): The degree of the polynomial curve to fit the data.

    Return Value:
    - str: A string representing the equation of the polynomial curve.
           The equation is in the form 'y = ax^n + bx^(n-1) + ... + cx + d'. Where d is a constant.
           
    Examples:
    >>> curve_fit(({"M_AVG": 4, "CACH": 1}, {"M_AVG": 9, "CACH": 2}, {"M_AVG": 16, "CACH": 3}), "CACH", 3)
        'y= x^2 + 2x + 1'
    >>> curve_fit(({"M_AVG": 7, "CACH": 0}, {"M_AVG": 0, "CACH": 1}, {"M_AVG": -9, "CACH": 2}, {"M_AVG": 4, "CACH": 3}), "CACH", 5)
        'y = 4x^3 - 13x^2 + 2x + 7'
    >>>  curve_fit(({"M_AVG": 3, "CACH": 0}, {"M_AVG": 4, "CACH": 1}, {"M_AVG": 5, "CACH": 2}), "CACH", 1)
         'y= x + 3'
    """
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
