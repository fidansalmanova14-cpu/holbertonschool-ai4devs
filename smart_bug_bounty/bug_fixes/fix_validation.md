# Fix Validation Report

## bug1.py
- **Original Issue**: Off-by-one error in slicing.
- **Fix Applied**: Implemented negative slicing `items[-n:]`.
- **Validation**: Verified with unit tests; returns expected list segments.

## bug2.js
- **Original Issue**: 'var' keyword caused closure bugs in loop.
- **Fix Applied**: Switched to `let` to ensure block scope.
- **Validation**: Console logs 0, 1, 2 as intended after delay.

## bug3.py
- **Original Issue**: Shared state via mutable default arguments.
- **Fix Applied**: Set default to `None` and initialized locally.
- **Validation**: Independent function calls no longer share data.

## bug4.c
- **Original Issue**: Buffer overflow with `strcpy`.
- **Fix Applied**: Increased buffer capacity and added `strlen` check.
- **Validation**: Program executes without memory corruption.
