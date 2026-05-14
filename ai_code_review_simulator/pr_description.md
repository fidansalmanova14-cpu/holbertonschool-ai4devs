# Pull Request: Add Library Management System Feature

## Summary
Implements a core Library Management System that allows adding books, searching by multiple criteria, managing checkouts with due dates, and tracking overdue items.

## Changes
- Created `Book` and `Library` classes in `library_manager.py`.
- Implemented `add_book`, `search_books`, `checkout_book`, and `return_book` methods.
- Added an internal audit log for library actions.
- Added 5 comprehensive unit tests in `test_library.py`.

## Context
~100 LOC. This feature serves as the foundation for the upcoming library digital platform.
