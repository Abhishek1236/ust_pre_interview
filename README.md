Python Algorithms
This project contains various algorithms and demonstrates how to use them in a multithreading context. The project includes:

Fibonacci sequence generator.
Search function to find a number in a list.
Email validation function.
Character occurrence counter.
The project is organized into different components, including:

The main execution script.
Multithreading to run multiple algorithms concurrently.
Input files to read data from.
Unit tests for validating functions.
Project Structure
bash
Copy code
project/
├── algorithms/
│   ├── algorithm1.py          # Contains the Fibonacci sequence function
│   ├── algorithm2.py          # Contains the search number function
│   ├── main.py                # Main script to run algorithms
│   └── multithreading.py      # Multithreading script to run tasks concurrently
├── input/
│   ├── email.txt             # Contains email addresses to validate (one per line)
│   └── string.txt            # Contains strings to count character occurrences
└── test/
    └── unittest.py            # Unit tests for validate_email and count_character_occurrences
Description
Algorithms:
Fibonacci Sequence (algorithm1.py):

Generates the Fibonacci sequence up to the nth term.
Search Number in List (algorithm2.py):

Searches for a number in a list and returns its index if found.
Validate Email (validate_email.py):

Validates an email address using a regular expression.
Character Occurrences (character_counter.py):

Counts the occurrences of each character in a given string.
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Abhishek1236/ust_pre_interview.git
cd python-algorithms
Install dependencies (if any) by running:

bash
Copy code
pip install -r requirements.txt
Usage
1. Running the Main Program:
To execute the main program that runs the algorithms, use:
bash
Copy code
python algorithms/main.py
2. Multithreading Execution:
If you want to run the email validation and character counting functions concurrently, use:

bash
Copy code
python algorithms/multithreading.py
This script uses Python’s threading module to execute both functions in parallel, improving performance by handling I/O operations simultaneously.

3. Input Files:
input/email.txt: Contains email addresses to validate (one per line).
input/string.txt: Contains the string whose character occurrences you want to count.
4. Unit Tests:
The unit tests are written in test/unittest.py.
To run the unit tests for validating the validate_email and count_character_occurrences functions, execute:
bash
Copy code
python -m unittest test/unittest.py
Example Input Files
input/email.txt
graphql
Copy code
example@example.com
user.name@domain.com
invalid-email.com
another.example@domain
input/string.txt
Copy code
hello world
Tests
The project includes unit tests for the core functions:

validate_email: Validates multiple email addresses, including both valid and invalid examples.
count_character_occurrences: Validates the correct counting of characters in various strings:
A normal string ("hello world").
An empty string ("").
A string with special characters ("aabb@@cc##").
To run the tests, execute:

bash
Copy code
python -m unittest test/unittest.py
Multithreading Example
The multithreading.py script demonstrates the use of multithreading to run the email validation and character counting functions concurrently. This allows the program to handle I/O-bound tasks more efficiently by processing them in parallel.

Requirements
Python 3.x
unittest (for running unit tests)
threading (built-in module for multithreading)
For any additional dependencies, you can add them to the requirements.txt file.

