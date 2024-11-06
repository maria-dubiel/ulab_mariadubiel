# file: even_sum.py
import numpy as np

def sum_even_numbers(numbers):
    """
    returns the sum of all even numbers in a given list or array.
    Inputs: 
    outputs:
    """

    sum = np.sum(num for num in numbers if num % 2 == 0) #putting this in a file vs notebook allows us to import the function
    return sum