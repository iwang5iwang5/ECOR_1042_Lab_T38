# ECOR 1042 Lab 4 - team submission

#import check module here
import check

#import load_data module here
import load_data

# Update "" with your the name of the active members of the team
__author__ = "Ivan Wang, Stefan Martincevic, Lance Downton, Esosa Ohangbon"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-038"

#==========================================#

# Place test_return_list function here 

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

# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght() -> None:
    # Complete the function with your test cases
    check.equal(len(load_data.machine_vendor_list(
        'machine-test.csv', 'amdahl')), 9)
    check.equal(len(load_data.machine_vendor_list(
        'machine-test.csv', 'apollo')), 1)
    check.equal(len(load_data.machine_vendor_list(
        'machine-test.csv', 'zumba')), 0)

    check.equal(len(load_data.machine_model_list(
        'machine-test.csv', '470v/7')), 1)
    check.equal(len(load_data.machine_model_list(
        'machine-test.csv', '580-5840')), 4)
    check.equal(len(load_data.machine_model_list(
        'machine-test.csv', 'rumba')), 0)

    check.equal(len(load_data.machine_cache_list('machine-test.csv', 0)), 22)
    check.equal(len(load_data.machine_cache_list('machine-test.csv', 142)), 1)
    check.equal(len(load_data.machine_cache_list(
        'machine-test.csv', 64920)), 0)

    check.equal(len(load_data.machine_prp_list('machine-test.csv', 1144)), 1)
    check.equal(len(load_data.machine_prp_list('machine-test.csv', 150)), 8)
    check.equal(len(load_data.machine_prp_list('machine-test.csv', 4761)), 0)

    check.equal(len(load_data.load_data(
        'machine-test.csv', ('MYCT', 20))), 0)
    check.equal(len(load_data.load_data(
        'machine-test.csv', ('CACH', 32))), 12)
    check.equal(len(load_data.load_data(
        'machine-test.csv', ('Model', '8000'))), 1)
    check.equal(len(load_data.load_data(
        'machine-test.csv', ('prp', 100))), 11)
    check.equal(len(load_data.load_data(
        'machine-test.csv', ('Model', '580-5840'))), 4)
    check.equal(len(load_data.load_data(
        'machine-test.csv', ('all', 'hello'))), 22)

    check.equal(len(load_data.add_average_main_memory([])), 0)
    check.equal(len(load_data.add_average_main_memory([{'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381}, {
                'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238}])), 4)
    check.equal(len(load_data.add_average_main_memory(
        [{'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}])), 1)

    check.summary()

#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    #Complete the function with your test cases

    #vendor test
    test = load_data.machine_vendor_list("machine-test.csv", "apollo")
    expected = ({"Model":"dn320","MYCT":400,"MMIN":1000,"MMAX":3000,"CACH":0,"PRP":38,"ERP":23},{"Model":"dn320","MYCT":400,"MMIN":1000,"MMAX":3000,"CACH":0,"PRP":38,"ERP":23})
    check.equal((test[0],test[-1]), expected)

    test = load_data.machine_vendor_list("machine-test.csv", "non")
    expected = ([])
    check.equal((test), expected)

    test = load_data.machine_vendor_list("machine-test.csv", "bti")
    expected = ({"Model":"5000","MYCT":350,"MMIN":64,"MMAX":64,"CACH":0,"PRP":10,"ERP":15},{"Model":"8000","MYCT":200,"MMIN":512,"MMAX":16000,"CACH":0,"PRP":35,"ERP":64})
    check.equal((test[0],test[-1]), expected)

    #model test
    test = load_data.machine_model_list("machine-test.csv", "dn320")
    expected = ({"Vendor":"apollo","MYCT":400,"MMIN":1000,"MMAX":3000,"CACH":0,"PRP":38,"ERP":23},{"Vendor":"apollo","MYCT":400,"MMIN":1000,"MMAX":3000,"CACH":0,"PRP":38,"ERP":23})
    check.equal((test[0],test[-1]), expected)

    test = load_data.machine_model_list("machine-test.csv", "non")
    expected = ([])
    check.equal((test), expected)

    test = load_data.machine_model_list("machine-test.csv", "580-5840")
    expected = ({"Vendor":"amdahl","MYCT":23,"MMIN":16000,"MMAX":32000,"CACH":64,"PRP":367,"ERP":381},{"Vendor":"amdahl","MYCT":23,"MMIN":32000,"MMAX":64000,"CACH":128,"PRP":1144,"ERP":1238})
    check.equal((test[0],test[-1]), expected)

    #cache test
    test = load_data.machine_cache_list("machine-test.csv", 141)
    expected = ({'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124},{'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})
    check.equal((test[0],test[-1]), expected)

    test = load_data.machine_cache_list("machine-test.csv", 200)
    expected = ([])
    check.equal((test), expected)

    test = load_data.machine_cache_list("machine-test.csv", 0)
    expected = ({'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'PRP': 76, 'ERP': 45})
    check.equal((test[0],test[-1]), expected)
    
    #prp test
    test = load_data.machine_prp_list("machine-test.csv", 1143)
    expected = ({'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238},{'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238})
    check.equal((test[0],test[-1]), expected)

    test = load_data.machine_prp_list("machine-test.csv", 2000)
    expected = ([])
    check.equal((test), expected)

    test = load_data.machine_prp_list("machine-test.csv", 0)
    expected = ({'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45})
    check.equal((test[0],test[-1]), expected)

    #load_data test
    test = load_data.load_data("machine-test.csv", ("all",-1))
    expected = ({'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45})
    check.equal((test[0],test[-1]), expected)

    test = load_data.load_data("machine-test.csv", ("Vendor", "basf"))
    expected = ({'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70},{'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117})
    check.equal((test[0],test[-1]), expected)

    test = load_data.load_data("machine-test.csv", ("Model", "b6925"))
    expected = ({'Vendor': 'burroughs', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45},{'Vendor': 'burroughs', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45})
    check.equal((test[0],test[-1]), expected)

    test = load_data.load_data("machine-test.csv", ("cach", 127))
    expected = ({'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238},{'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})
    check.equal((test[0],test[-1]), expected)

    test = load_data.load_data("machine-test.csv", ("prp", 635))
    expected = ({'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238})
    check.equal((test[0],test[-1]), expected)

    test = load_data.load_data("machine-test.csv", ("invalid", 0))
    expected = ([])
    check.equal((test), expected)

    #load_data test
    test = load_data.add_average_main_memory([{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}])
    expected = ({'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
                 'CACH': 256, 'PRP': 198, 'ERP': 199, 'M_AVG': 3128.0}, {'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
                 'CACH': 256, 'PRP': 198, 'ERP': 199, 'M_AVG': 3128.0})
    check.equal((test[0],test[-1]), expected)

    test = load_data.add_average_main_memory([])
    expected = ([])
    check.equal((test), expected)

    test = load_data.add_average_main_memory([{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
        'CACH': 256, 'PRP': 198, 'ERP': 199},
      {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 269, 'ERP': 253}, 
      {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
        'CACH': 32, 'PRP': 220, 'ERP': 253}
    ])
    expected = ({'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 
        'CACH': 256, 'PRP': 198, 'ERP': 199, 'M_AVG': 3128.0}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 
      'CACH': 32, 'PRP': 220, 'ERP': 253, 'M_AVG': 20000.0})
    check.equal((test[0],test[-1]), expected)

    check.summary()



#Place test_add_average function here
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
