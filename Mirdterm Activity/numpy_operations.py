#ACTIVITY 8 IMPORTED SCRIPT

# numpy_operations.py
import numpy as np

def create_array(size=10, low=0, high=100):
    """
    Creates a NumPy array with specified size and range.
    
    Parameters:
    size (int): Number of elements (default: 10)
    low (float): Lower bound (default: 0)
    high (float): Upper bound (default: 100)
    
    Returns:
    numpy.ndarray: Random array
    """
    return np.random.uniform(low, high, size)

def calculate_statistics(array):
    """
    Calculates various statistics for a NumPy array.
    
    Parameters:
    array (numpy.ndarray): Input array
    
    Returns:
    dict: Dictionary with statistical measures
    """
    return {
        'mean': np.mean(array),
        'std': np.std(array),
        'min': np.min(array),
        'max': np.max(array),
        'median': np.median(array)
    }