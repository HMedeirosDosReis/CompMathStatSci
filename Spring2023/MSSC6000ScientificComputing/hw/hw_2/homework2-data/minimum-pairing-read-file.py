def read_data(file_name):
    """
    reads in the file at <file_name> and returns a list of two lists, e.g.
    [[1, 2, 3], [4, 5, 6]]
    """

    with open(file_name, "r") as f:
        list1 = list(map(int, f.readline().strip().split(" ")))
        list2 = list(map(int, f.readline().strip().split(" ")))
    return [list1, list2]
