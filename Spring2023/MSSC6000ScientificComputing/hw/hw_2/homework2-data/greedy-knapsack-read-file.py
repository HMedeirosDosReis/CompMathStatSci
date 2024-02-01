def read_data(file_name):
    """
    reads in the file at <file_name> and returns a tuple wih two entries
    - the first entry is the capacity of the knapsack (a float)
    - the second entry is a list of 3-tuples, (name, weight, value), a string and two
        floats, for each item
    """

    capacity = 0
    items = []

    with open(file_name, "r") as f:
        capacity = float(f.readline().strip())
        for line in f:
            data = line.strip()
            if data:
                split_data = data.split(" ")
                items.append(
                    (split_data[0], float(split_data[1]), float(split_data[2]))
                )

    return (capacity, items)
