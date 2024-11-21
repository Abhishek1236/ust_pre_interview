def count_characters_string(input_string):
    """
    Count the occurence of character in the input string
    """
    char_count = {}
    for character in input_string:
        char_count[character] = char_count.get(character,0) + 1
    return char_count