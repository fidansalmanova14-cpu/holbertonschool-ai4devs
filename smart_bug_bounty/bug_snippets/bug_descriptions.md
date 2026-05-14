# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last n items in a list.
- **Current Issue**: Off-by-one error due to incorrect slicing index.

## bug2.js
- **Intended Behavior**: Print numbers 0, 1, 2 with a delay.
- **Current Issue**: Using 'var' in a loop with setTimeout causes closure issues, printing '3' three times.

## bug3.py
- **Intended Behavior**: Create a new list for each function call if no list is provided.
- **Current Issue**: Mutable default argument 'box' persists across function calls.

## bug4.c
- **Intended Behavior**: Copy a string into a buffer and print it.
- **Current Issue**: Buffer overflow because the source string exceeds the 10-byte buffer size.
