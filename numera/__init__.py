def mean_deviation(data) -> float:
    """
    Calculates the arithmetic mean (average) of a given dataset.

    Parameters:
    data (list of numbers): A list of numerical values.

    Returns:
    float: The arithmetic mean of the numbers in the dataset.
    
    Example:
    >>> mean_deviation([1, 2, 3, 4, 5])
    3.0
    """
    return sum(data) / len(data)
