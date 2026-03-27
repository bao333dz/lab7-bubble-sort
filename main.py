import os
import time

arr = [1,9,6,7,2,5,8]

def color(i: int, unsorted: bool):
    os.system('cls')
    Yellow = "\033[93m"
    Green = "\033[32m"
    Reset = "\033[0m"
    for y in range(0, len(arr)):
        if y == i or y == i + 1:
            print(f"{Yellow}{'▆' * arr[y]}{Reset}")
        else:
            print('▆' * arr[y])
    print("Current state:", arr)

    if unsorted == False:
        os.system('cls')
        for a in range (0, len(arr)):
            print(f"{Green}{'▆' * arr[a]}{Reset}")

    time.sleep(0.5)

def bubble(arr):
    """
    Sorts a list using the bubble sort algorithm with visualization.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        The sorted list (sorted in-place)
    """
    unsorted = True
    while unsorted:
        swap_count = 0
        for i in range(0, len(arr) - 1):
            color(i, unsorted)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_count += 1
                color(i, unsorted)
        if swap_count == 0:
            unsorted = False
            color(i, unsorted)
    return print("Done, the sorted version is:", arr)


bubble(arr)