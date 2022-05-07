#!/usr/bin/python3
""" Filtering DATA acording to the functions descriptions.
    """


from database import DATA


def python_devs(DATA):
    """ Print a list with the python developers
        """
    # Using list comprehension:
    python_devs_lc = [worker['name'] for worker in DATA if worker['language'] == 'python']
    print(f"Python-Devs (list comprehension): {python_devs_lc}")

    # Using filter and map:
    python_devs_f = list(filter(lambda worker: worker['language'] == 'python', DATA))
    python_devs_m = list(map(lambda worker: worker['name'], python_devs_f))
    print(f"Python-Devs (filter & map): {python_devs_m}")


def platzi_workers(DATA):
    """ Print a list with the Platzi workers
        """
    # Using list comprehension
    platzi_workers_lc = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print(f"Platzi workers (list comprehension): {platzi_workers_lc}")
    
    # Using filter and map:
    platzi_workers_f = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    platzi_workers_m = list(map(lambda worker: worker['name'], platzi_workers_f))
    print(f"Platzi workers (filter & map): {platzi_workers_m}")


def adults(DATA):
    """ Print people older than 18
        """
    # Using filter and map:
    adults_f = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults_m = list(map(lambda worker: worker['name'], adults_f))
    print(f"Adults (filter & map): {adults_m}")

    # Using list comprehension:
    adults_lc = [worker['name'] for worker in DATA if worker['age'] > 18]
    print(f"Adults (list comprehension): {adults_lc}")


def old_people(DATA):
    """ Add a new key/value to DATA where key is 'old' and value is True or False
        if the age is greater than 70. Print only their names.
        """
    # Using filter and map:
    old_people_m = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    old_people_f = list(filter(lambda worker: worker['old'] == True, old_people_m))
    old_people_names = list(map(lambda worker: worker['name'], old_people_f))
    print(f"Old people (filter & map): {old_people_names}")

    # Using list comprehension:
    old_people_lc = [worker | {'old': worker['age'] > 70} for worker in DATA]
    old_people_name = [worker['name'] for worker in old_people_lc if worker['old'] == True]
    print(f"Old people (list comprehension): {old_people_name}")


if __name__ == '__main__':
    python_devs(DATA)
    platzi_workers(DATA)
    adults(DATA)
    old_people(DATA)
