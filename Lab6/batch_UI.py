# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ivan Wang"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298751"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
# Place your script for your batch_UI after this line
import curve_fit
import histogram
import load_data
import sort

def load_data_command(e:list):
    pass
def curve_fit_command(e:list):
    pass
def histogram_command(e:list):
    pass
def sort_command(e:list):
    pass

# filename = input("Please enter the name of the file where your commands are stored: ")
filename = "batch.txt"
with open(filename, "r") as batch:
    commands = batch.read().strip().split("\n")
    for i in range(len(commands)):
        commands[i] = commands[i].strip().split(";")
    print(commands)

    not_exit = True
    i = 0

    while i < len(commands) and not_exit:
        if commands[i][0] == "L":
            load_data_command(commands[i])
        elif commands[i][0] == "S":
            sort_command(commands[i])
        elif commands[i][0] == "C":
            curve_fit_command(commands[i])
        elif commands[i][0] == "H":
            histogram_command(commands[i])
        elif commands[i][0] == "E":
            not_exit = False
        i += 1