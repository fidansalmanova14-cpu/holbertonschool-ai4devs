# Benchmark Tasks - Copilot Productivity Sprint

## Task 1: Data Processing Script
**Requirements**: Create a Python script that reads a CSV file of student grades, calculates the average score for each student, and saves the results to a new JSON file.
**Inputs**: `students.csv` (Columns: Name, Math, Science, English)
**Outputs**: `averages.json`
**Acceptance Criteria**:
- Successfully calculates the mean of three subjects.
- Handles missing values by treating them as 0.
- JSON output is properly formatted.

---

## Task 2: String Manipulation Utility
**Requirements**: Write a function that takes a long string and returns a dictionary with the frequency of each word, excluding common "stop words" (a, an, the, is, in).
**Inputs**: A paragraph of text (string).
**Outputs**: Dictionary `{word: count}`.
**Acceptance Criteria**:
- Case-insensitive matching.
- Removes punctuation before counting.
- Correctly filters out the specified stop words.

---

## Task 3: Simple API Unit Tests
**Requirements**: Write a set of unit tests using `pytest` for a pre-defined User class that has methods for `set_email` (with regex validation) and `is_adult` (checks age >= 18).
**Inputs**: Python `User` class.
**Outputs**: Test suite file `test_user.py`.
**Acceptance Criteria**:
- At least 5 test cases covering valid/invalid emails.
- Test cases for boundary ages (17, 18, 19).
- All tests pass when run with `pytest`.
