# ECOR 1042 Lab 3 - Template


# Update
__author__ = "Esosa Ohangbon"
__student_number__ = "101297277"
__team__ = "T038"

#==========================================#
# Place your machine_prp_list function after this line
#......

def machine_prp_list(file_name, min_performance):
    """
    Return a list of dictionaries, each representing a machine with attributes meeting the minimum performance provided by the user.

    Arguments:
    - file_name (str): The name of the file containing machine data in CSV format.
    - min_performance (int): The minimum acceptable published relative performance.

    Examples:
    >>> machine_prp_list('machine.csv', 150)
    [   {'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256,
        'MMAX': 6000, 'CACH': 256, 'ERP':199},
        {another element},
        …
    ]
    >>> machine_prp_list('machine.csv', 1500)
        []

    """

    machines = []

    # Read data from the CSV file
    with open(file_name, 'r') as file:
        line = file.readline()
        headers = line.strip().split(',')

        for lines in file:
            # Convert 'PRP' to integer for comparison
            values = lines.strip().split(',')
            machine = {}
            if int(values[6]) >= min_performance:
                for i in range(len(headers)):
                    if headers[i] != 'PRP':
                        try:
                            value = int(values[i])
                        except:
                            value = values[i]
                        machine[headers[i]] = value
                machines += [machine]

    return machines


# Do not include a main script
