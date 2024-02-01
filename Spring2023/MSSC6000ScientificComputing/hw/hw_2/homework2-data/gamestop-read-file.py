def read_data(file_name):
    """
    Reads in the file at <file_name> and returns a list of tuples of length two of the
    form (money, wait_time).

    A wait time of 0 means the customer will leave if not served first.
    A wait time of 1 means the customer will leave if not served first or second.
    etc.
    """

    customers = []
    with open(file_name, "r") as f:
        for line in f:
            data = line.strip().split(" ")
            if data:
                customers.append((int(data[0]), int(data[1])))
    return customers
