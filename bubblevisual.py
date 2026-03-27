import pygame
from typing import List, Tuple


def display_bubble_sort(arr: List[int], i: int = -1, unsorted: bool = True, 
                        window_width: int = 800, window_height: int = 600) -> None:
    """
    Display bubble sort visualization using pygame.
    
    Args:
        arr: The array being sorted
        i: Index of the element currently being compared (-1 if no comparison active)
        unsorted: Whether the array is still being sorted
        window_width: Width of the pygame window
        window_height: Height of the pygame window
    
    Returns:
        None
    """
    # TODO: Initialize pygame if not already done
    # TODO: Create or get the display surface
    
    # TODO: Calculate bar dimensions based on array size and window size
    
    # TODO: Draw background (white or light color)
    
    # TODO: Draw bars for each element
    #   - Normal bars: light gray
    #   - Bars at index i and i+1: yellow (being compared)
    #   - All bars: green when unsorted == False (sorted complete)
    
    # TODO: Display current array state as text
    
    # TODO: Update the display with pygame.display.flip()
    
    pass
