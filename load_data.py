# ECOR 1042 Lab 3 - Template


# Update "" to list all students contributing to the team work
__author__ = ""

# Update "" with your team (e.g. T102)
__team__ = "Sample"

#==========================================#
# Place your machine_vendor_list function after this line



#==========================================#
# Place your machine_model_list function after this line


#==========================================#
# Place your machine_cache_list function after this line



#==========================================#
# Place your machine_prp_list function after this line



#==========================================#
# Place your load_data function after this line


#==========================================#
# Place your add_average_main_memory function after this line
def add_average_main_memory(machines: list[dict]) ->list[dict]:
    """Return list of machines with a new entry added to each dictionary.
    The new entry's key is 'M_AVG' with the value of the average of the memory usage.
    
    """
    for machine in machines:
        machine['M_AVG'] = (machine['MMAX'] + machine['MMIN']) / 2
    return machines
    


# Do NOT include a main script in your submission


