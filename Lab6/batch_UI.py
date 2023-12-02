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
    if not e[2].lower() in ["vendor", "model","cach", "prp", "all"]:
        return []
    if len(e) == 4:
        data = load_data.add_average_main_memory(load_data.load_data(e[1], (e[2],e[3]))) 
    else:
        data = load_data.add_average_main_memory(load_data.load_data(e[1], (e[2],-1)))
    if len(data) > 0:
        print("Data loaded")
        return data
    return data

# def curve_fit_command(e:list):
    # return curve_fit.curvefit()

# def histogram_command(e:list):
#     return histogram.histogram()

def sort_command(e:list, data: list[dict]):
    if data == []:
        print("File not loaded. Please, load a file first.")
        return []
    if e[3].lower() == "n":
        return sort.sort(data,e[2],e[1])
    elif e[3].lower() == 'y':
        data = sort.sort(data,e[2],e[1])
        print(data)
        return data

# filename = input("Please enter the name of the file where your commands are stored: ")
filename = "batch.txt"
with open(filename, "r") as batch:
    commands = batch.read().strip().split("\n")
    for i in range(len(commands)):
        commands[i] = commands[i].strip().split(";")
    print(commands)

    not_exit = True
    i = 0
    data = []

    while i < len(commands) and not_exit:
        if commands[i][0].upper() == "L":
            data = load_data_command(commands[i])
        elif commands[i][0].upper() == "S":
            sort_command(commands[i], data)
        # elif commands[i][0].upper() == "C":
        #     curve_fit_command(commands[i])
        # elif commands[i][0].upper() == "H":
        #     histogram_command(commands[i])
        elif commands[i][0].upper() == "E":
            not_exit = False
        else:
            print("Invalid command.")
        i += 1