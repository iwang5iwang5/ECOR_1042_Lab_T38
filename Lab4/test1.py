# ECOR 1042 Lab 4 - Individual submission for test1 function

# import check module here
import check
# import load_data module here
import load_data
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Esosa Ohangbon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297277"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#
# Do not modify the code alreayd provided.


def test_return_list():
    # Complete the function with your test cases
    vendor_test1 = load_data.machine_vendor_list("machine-test.csv", "basf")
    check.equal(type(vendor_test1), list)
    vendor_test2 = load_data.machine_vendor_list("machine-test.csv", "reek")
    check.equal(type(vendor_test2), list)
    vendor_test3 = load_data.machine_vendor_list(
        "machine-test.csv", "apollo")
    check.equal(type(vendor_test3), list)

    model_test1 = load_data.machine_model_list("machine-test.csv", 5000)
    check.equal(type(model_test1), list)
    model_test2 = load_data.machine_model_list(
        "machine-test.csv", "580-5840")
    check.equal(type(model_test2), list)
    model_test3 = load_data.machine_model_list("machine-test.csv", "b0000")
    check.equal(type(model_test3), list)

    cache_test1 = load_data.machine_cache_list("machine-test.csv", 32)
    check.equal(type(cache_test1), list)
    cache_test2 = load_data.machine_cache_list("machine-test.csv", 200)
    check.equal(type(cache_test2), list)
    cache_test3 = load_data.machine_cache_list("machine-test.csv", 142)
    check.equal(type(cache_test3), list)

    prp_test1 = load_data.machine_prp_list("machine-test.csv", 1200)
    check.equal(type(prp_test1), list)
    prp_test2 = load_data.machine_prp_list("machine-test.csv", 1144)
    check.equal(type(prp_test2), list)
    prp_test3 = load_data.machine_prp_list("machine-test.csv", 172)
    check.equal(type(prp_test3), list)

    load_data_test1 = load_data.load_data("machine-test.csv", ("CACH", 32))
    check.equal(type(load_data_test1), list)
    load_data_test2 = load_data.load_data("machine-test.csv", ("PRP", 269))
    check.equal(type(load_data_test2), list)
    load_data_test3 = load_data.load_data(
        "machine-test.csv", ("MODEL", "Jul-65"))
    check.equal(type(load_data_test3), list)
    load_data_test4 = load_data.load_data(
        "machine-test.csv", ("VENDOR", "amdahl"))
    check.equal(type(load_data_test4), list)
    load_data_test5 = load_data.load_data("machine-test.csv", ("All", 2000))
    check.equal(type(load_data_test5), list)
    load_data_test6 = load_data.load_data("machine-test.csv", ("MMIN", 512))
    check.equal(type(load_data_test6), list)

    add_average_main_memory_test1 = load_data.add_average_main_memory(
        load_data.machine_vendor_list("machine-test.csv", "basf"))
    check.equal(type(add_average_main_memory_test1), list)
    add_average_main_memory_test2 = load_data.add_average_main_memory(
        load_data.machine_model_list("machine-test.csv", "apollo"))
    check.equal(type(add_average_main_memory_test2), list)
    add_average_main_memory_test3 = load_data.add_average_main_memory(
        load_data.machine_prp_list("machine-test.csv", 2000))
    check.equal(type(add_average_main_memory_test3), list)

    check.summary()


# Do NOT include a main script in your submission
