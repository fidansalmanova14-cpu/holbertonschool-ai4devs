Bug 1 – apply_discount (Python)
Intended Behavior: Calculate the discount amount based on a percentage and subtract it from the original price to return the correct final price.

Issue Type: Logical Error.

Notes: The code calculates the discount_amount correctly but fails to use it. Instead, it subtracts the raw percentage value (e.g., subtracting 10 from 1200 instead of 120).

Bug 2 – displayUserBios (JavaScript)
Intended Behavior: Iterate through a list of users and print their biographies, safely handling cases where a profile or bio might be missing.

Issue Type: Runtime Error (TypeError).

Notes: The code attempts to access user.profile.bio directly. Since some users have a null profile or no profile at all, the program crashes when trying to read a property of null or undefined.

Bug 3 – system_diagnostic_report (Python)
Intended Behavior: Identify the operating system and print the CPU count using proper Python syntax and structure.

Issue Type: Syntax Error / Indentation Error.

Notes: The script is missing colons (:) at the end of the if and else statements. Additionally, the indentation for the print statements is inconsistent, which prevents the code from executing.

Bug 4 – main.c (C)
Intended Behavior: Loop through a 5-element array to print each score and calculate the total sum.

Issue Type: Out-of-bounds Error (Buffer Overflow/Off-by-one).

Notes: The loop condition i <= num_elements causes the program to access scores[5]. Since C arrays are zero-indexed, a 5-element array only has indices 0 through 4. This results in reading "garbage" data from memory or a program crash.
