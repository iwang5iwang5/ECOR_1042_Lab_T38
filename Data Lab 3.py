# ECOR 1042 Lab 3 - Template


# Update
__author__ = "Stefan Martincevic"
__student_number__ = "101295641"
__team__ = "T 38"

#==========================================#


def machine_vendor_list(filename: str, param: str) -> list[{}]:
    """
    Return a list of machines that belong to a specifc vendor. Return an empty list if the vendor does not exist.

    Preconditions: None

    >>> machine_vendor_list(machine.csv, amdahl)
    [{'Model': '32/60', 'MYCT': '125', 'MMIN': '256', 'MMAX': '6000', 'CACH': '256', 'PRP': '198', 'ERP': '199'}]
    >>> machine_vendor_list(machine.csv, apollo)
    [{'Model': 'dn320', 'MYCT': '400', 'MMIN': '1000', 'MMAX': '3000', 'CACH': '0', 'PRP': '38', 'ERP': '23'}, {'Model': 'dn420', 'MYCT': '400', 'MMIN': '512', 'MMAX': '3500', 'CACH': '4', 'PRP': '40', 'ERP': '24'}]
    >>> machine_vendor_list(machine.csv, bti)
    [{'Model': '5000', 'MYCT': '350', 'MMIN': '64', 'MMAX': '64', 'CACH': '0', 'PRP': '10', 'ERP': '15'}, {'Model': '8000', 'MYCT': '200', 'MMIN': '512', 'MMAX': '16000', 'CACH': '0', 'PRP': '35', 'ERP': '64'}]
    """
    infile = open(filename, "r")
    header = infile.readline().strip().split(",")
    result = []
    for line in infile:
        line_lst = line.strip().split(",")
        if line_lst[0] == param:
            data = {}
            for i in range(1, len(header)):
                data[header[i]] = line_lst[i]

            result.append(data)
    infile.close()
    return result


vendor = 'bti'
print(machine_vendor_list('machine.csv', vendor))
