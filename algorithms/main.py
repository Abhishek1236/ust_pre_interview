from algorithm1 import count_characters_string
from algorithm2 import validate_email


def main():
    #Validate email ID 
    email_file_path = "algorithms\inputs\email.txt" 
    try:
        with open(email_file_path,"r") as file:
            email = file.read().strip()
    except FileNotFoundError:
        print(f"Eror : File '{email_file_path}' not found")

    is_valid = validate_email(email)

    if is_valid:
        print(f"The email {email} is valid")
    else:
        print(f"The email id {email} is not valid")

    # Count occurence
    string_file_path = "algorithms\inputs\string.txt"
    try:
        with open(string_file_path,"r") as file:
            input_string = file.read().strip()
    except FileNotFoundError:
        print(f"Eror : string '{string_file_path}' not found")
    char_count = count_characters_string(input_string)
    print(f"Character occurence in {input_string} is :")
    for character,count in char_count.items():
        print(f"'{character}':{count}")


if __name__ == "__main__":
    main()