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


def variance(data, sample: bool = False) -> float | int:
    """
    Calculates the variance of a given dataset.

    Args:
        data (list or iterable of numbers): 
            The dataset for which the variance will be calculated.
        sample (bool, optional): 
            Determines whether to calculate the sample variance (`True`) or 
            the population variance (`False`). Defaults to `False`.

    Returns:
        float:
            The variance of the dataset.

    Example:
        >>> variance([1, 2, 3, 4, 5], sample=False)
        2.0
    """
    avrg = mean_deviation(data)
    total = sum((avrg - number) ** 2 for number in data)
    return total / (len(data) - 1) if sample else total / len(data)

    
def standard_deviation(data, sample:bool = False) -> float | int:
    """
    This func calculate standard_deviation of a dataset

    Args:
        data (list or iterable of numbers): 
            The dataset for which the standard_deviation will be calculated.
        sample (bool, optional): 
            Determines whether to calculate the sample standard_deviation (`True`) or 
            the population standard_deviation (`False`). Defaults to `False`.

    Returns:
        float | int: _description_
        
    Example
    >>> standard_deviation([1,2,3,4,5], sample:bool = False)
    1.4142135623730951
    """
    return variance(data, sample) ** 0.5