def sort_by_age(tuples_list):
    """
    Sorts a list of tuples by age in ascending order.

    Args:
        tuples_list (list): The list of tuples to sort.

    Returns:
        list: The sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: x[1])