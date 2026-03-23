import os
import time

arr = [4, 1, 3, 9, 7]


def clear_screen():
    """
    TODO: Clear the terminal screen (Windows: 'cls', Unix/Mac: 'clear')
    Use: os.system()
    """
    pass


def draw_bar_chart(arr, comparing_indices=None, swapped_indices=None):
    """
    TODO: Display array as ASCII bar chart
    
    Args:
        arr: List of numbers to visualize
        comparing_indices: Tuple (i, j) of indices currently being compared (highlight in yellow)
        swapped_indices: Tuple (i, j) of indices just swapped (highlight in green)
    
    Requirements:
    - Find max value in arr to scale bar lengths
    - Print each number with a bar of █ characters proportional to its value
    - Use ANSI color codes:
      * Yellow: comparing indices
      * Green: swapped indices
      * Default: other elements
    - Format: [value] ████████
    
    ANSI Color Codes:
    - Yellow: \033[93m
    - Green: \033[92m
    - Reset: \033[0m
    """
    pass


def visualize_state(arr, pass_num, comparing_indices=None, swapped_indices=None):
    """
    TODO: Orchestrate visualization update
    
    Args:
        arr: Current state of array
        pass_num: Current pass number
        comparing_indices: Indices being compared
        swapped_indices: Indices just swapped
    
    Requirements:
    - Clear screen
    - Print pass information (e.g., "Pass 1: Comparing indices 0,1")
    - Draw bar chart
    - Add small delay (time.sleep()) for animation effect
    """
    pass


def bubble(arr):
    """
    Sorts a list using the bubble sort algorithm with visualization.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        The sorted list (sorted in-place)
    """
    pass_num = 0
    unsorted = True
    while unsorted:
        pass_num += 1
        swap_count = 0
        for i in range(0, len(arr) - 1):
            # TODO: Call visualize_state() here to show which elements are being compared
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_count += 1
                # TODO: Call visualize_state() here to highlight the swap that just happened
        if swap_count == 0:
            unsorted = False
    
    # TODO: Final visualization showing sorted array
    return arr


print(bubble(arr))