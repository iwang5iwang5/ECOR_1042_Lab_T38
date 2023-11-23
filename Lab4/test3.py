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

# Do NOT include a main script in your submission