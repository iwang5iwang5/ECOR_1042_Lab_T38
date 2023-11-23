# ECOR 1042 Lab 4 - Individual submission for test2 function

# import check module here

# import load_data module here

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Stefan Martincevic"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101295641"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T38"

#==========================================#
# Do not modify the code alreayd provided.
import check
import load_data


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

# Do NOT include a main script in your submission
