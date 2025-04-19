import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        this function return submatrix
        with start and end value
        print old shape matrix and new
    """
    try:
        if family is None or start is None or end is None:
            raise AssertionError("the arguments are bad")
        if not isinstance(family, list):
            raise AssertionError("not a list")
        matrix = np.array(family)
        print("My shape is : ", matrix.shape)
        submatrix = matrix[start:end, :]
        print("My new shape is : ", submatrix.shape)
        return submatrix.tolist()
    except AssertionError as ve:
        print("\033[91mAssertionError\033[0m", ve)
        return None
