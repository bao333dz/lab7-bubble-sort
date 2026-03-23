# Bubble Sort Implementation

A Python implementation of the bubble sort algorithm with comprehensive test coverage.

## Overview

This project implements the bubble sort algorithm, a simple comparison-based sorting technique that repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order. The algorithm terminates when a complete pass results in no swaps, indicating the list is sorted.

## Files

- **main.py** — Contains the `bubble()` function and example usage
- **test_bubble_sort.py** — Pytest test suite with 5 comprehensive test cases
- **JOURNAL.md** — Development log tracking all interactions and changes
- **REPORT.md** — Project report (if applicable)

## How It Works

The algorithm uses a swap counter to track whether any element swaps occurred during a pass:
- If `swap_count == 0` after a full pass, the list is sorted and the loop exits
- Otherwise, another pass is performed
- Time complexity: O(n²) worst/average case, O(n) best case (already sorted)

## Running the Code

### Execute the sorting algorithm:
```bash
python main.py
```

This will sort the example list `[4, 1, 3, 9, 7]` and print the result: `[1, 3, 4, 7, 9]`

### Run the test suite:
```bash
python -m pytest test_bubble_sort.py -v
```

## Test Coverage

The test suite validates:
1. **Unsorted lists** — correctly sorts randomly ordered elements
2. **Already sorted lists** — handles pre-sorted input efficiently
3. **Reverse sorted lists** — sorts backwards-ordered lists
4. **Empty lists** — handles edge case of empty input
5. **Single element** — handles lists with one element

All tests verify:
- Output is correctly sorted in ascending order
- No data is lost during sorting (all input elements present in output)

## Requirements

- Python 3.7+
- pytest (for running tests)

## Next Steps / Potential Optimizations

- Rename `lo` variable for clarity (currently represents loop control)
- Implement optimizations: track the last swap position to reduce unnecessary passes
- Add support for reverse sorting (descending order)
- Add type hints for better code documentation
