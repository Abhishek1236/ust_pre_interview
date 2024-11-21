import threading
from algorithm2 import validate_email
from algorithm1 import count_characters_string


def validate_email_task(email_file_path):
    """
    Task to validate an email read from a file.
    """
    try:
        with open(email_file_path, "r") as file:
            email = file.read().strip()
        is_valid = validate_email(email)
        result = f"The email '{email}' is {'valid' if is_valid else 'invalid'}."
        print(result)
    except FileNotFoundError:
        print(f"Error: File '{email_file_path}' not found.")


def count_characters_task(string_file_path):
    """
    Task to count characters in a string read from a file.
    """
    try:
        with open(string_file_path, "r") as file:
            input_string = file.read().strip()
        char_counts = count_characters_string(input_string)
        print(f"Character occurrences in '{input_string}':")
        for char, count in char_counts.items():
            print(f"'{char}': {count}")
    except FileNotFoundError:
        print(f"Error: File '{string_file_path}' not found.")


def main():
    # Define file paths
    email_file_path = "algorithms\inputs\email.txt"
    string_file_path = "algorithms\inputs\string.txt"

    # Create threads for each task
    email_thread = threading.Thread(target=validate_email_task, args=(email_file_path,))
    char_count_thread = threading.Thread(target=count_characters_task, args=(string_file_path,))

    # Start threads
    email_thread.start()
    char_count_thread.start()

    # Wait for threads to finish
    email_thread.join()
    char_count_thread.join()


if __name__ == "__main__":
    main()
