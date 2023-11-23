# ECOR 1042 Lab 4 - Individual submission for test4 function

#import check module here
import check

#import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Lance Downton"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295784"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
#Do not modify the code alreayd provided.

def test_add_average():
    #Complete the function with your test cases
    
    data = load_data.load_data
    average = load_data.add_average_main_memory

    # Check list length
    fail_message = "INFO: add_average_main_memory changed the length of the list"
    check.equal(len(average(data("machine-test.csv", ("vendor", "amdahl")))), len(data("machine-test.csv", ("vendor", "amdahl"))), fail_message)
    check.equal(len(average(data("machine-test.csv", ("model", "580-5840")))), len(data("machine-test.csv", ("model", "580-5840"))), fail_message)
    check.equal(len(average(data("machine-test.csv", ("cach", 65)))), len(data("machine-test.csv", ("cach", 65))), fail_message)
    check.equal(len(average(data("machine-test.csv", ("prp", 300)))), len(data("machine-test.csv", ("prp", 300))), fail_message)
    check.equal(len(average(data("machine-test.csv", ("all", "I am very cool :)")))), len(data("machine-test.csv", ("all", "I am very cool :)"))), fail_message)
    check.equal(len(average([])), len([]), fail_message)
    
    # Check dictionary length
    fail_message = "INFO: add_average_main_memory had an unexpected affect on the length of the dictionary"
    check.equal(len(average(data("machine-test.csv", ("vendor", "amdahl")))[0]), len(data("machine-test.csv", ("vendor", "amdahl"))[0]) + 1, fail_message)
    check.equal(len(average(data("machine-test.csv", ("model", "580-5840")))[0]), len(data("machine-test.csv", ("model", "580-5840"))[0]) + 1, fail_message)
    check.equal(len(average(data("machine-test.csv", ("cach", 65)))[0]), len(data("machine-test.csv", ("cach", 65))[0]) + 1, fail_message)
    check.equal(len(average(data("machine-test.csv", ("prp", 300)))[0]), len(data("machine-test.csv", ("prp", 300))[0]) + 1, fail_message)
    check.equal(len(average(data("machine-test.csv", ("all", "I am very cool :)")))[0]), len(data("machine-test.csv", ("all", "I am very cool :)"))[0]) + 1, fail_message)

    # Check memory average
    fail_message = "INFO: add_average_main_memory does not add the correct value to the dictionary"
    mmin = data("machine-test.csv", ("vendor", "apollo"))[0]["MMIN"]
    mmax = data("machine-test.csv", ("vendor", "apollo"))[0]["MMAX"]
    check.equal(average(data("machine-test.csv", ("vendor", "apollo")))[0]["M_AVG"], round((mmin + mmax) / 2, 2), fail_message)
    mmin = data("machine-test.csv", ("model", "Jul-65"))[0]["MMIN"]
    mmax = data("machine-test.csv", ("model", "Jul-65"))[0]["MMAX"]
    check.equal(average(data("machine-test.csv", ("model", "Jul-65")))[0]["M_AVG"], round((mmin + mmax) / 2, 2), fail_message)
    mmin = data("machine-test.csv", ("cach", 130))[0]["MMIN"]
    mmax = data("machine-test.csv", ("cach", 130))[0]["MMAX"]
    check.equal(average(data("machine-test.csv", ("cach", 130)))[0]["M_AVG"],round((mmin + mmax) / 2, 2), fail_message)
    mmin = data("machine-test.csv", ("prp", 700))[0]["MMIN"]
    mmax = data("machine-test.csv", ("prp", 700))[0]["MMAX"]
    check.equal(average(data("machine-test.csv", ("prp", 700)))[0]["M_AVG"], round((mmin + mmax) / 2, 2), fail_message)
    mmin = data("machine-test.csv", ("all", "I am very cool :)"))[0]["MMIN"]
    mmax = data("machine-test.csv", ("all", "I am very cool :)"))[0]["MMAX"]
    check.equal(average(data("machine-test.csv", ("all", "I am very cool :)")))[0]["M_AVG"], round((mmin + mmax) / 2, 2), fail_message)

    # Get the summary of all checks
    check.summary()

# Do NOT include a main script in your submission