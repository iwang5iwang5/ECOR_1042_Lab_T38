# ECOR 1042 Lab 4 - Individual submission for test3 function

#import check module here
import check

#import load_data module here
import load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ivan Wang"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101298751"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
#Do not modify the code alreayd provided.

def test_return_correct_dict_inside_list():
    #Complete the function with your test cases

    #vendor test
    test_1_1 = load_data.machine_vendor_list("machine-test.csv", "apollo")
    check.equal((test_1_1["Model"], test_1_1["ERP"]), ("dn320",23))

    test_1_2 = load_data.machine_vendor_list("machine.csv", "non")
    check.equal(test_1_2, [])

    test_1_3 = load_data.machine_vendor_list("machine.csv", "basf")
    for e in test_1_3:
        e = (e["Model"],e["ERP"])
    check.equal(test_1_3, [("Jul-65",70),("Jul-68",117)])


    check.summary()


# Do NOT include a main script in your submission
test_return_correct_dict_inside_list()