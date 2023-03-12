#!/usr/bin/python3

def multiple_returns(sentence):
    # Get the length of the sentence
    length = len(sentence)

    # Get the first character of the sentence, or None if the sentence is empty
    first_char = sentence[0] if length > 0 else None

    # Return the tuple
    return (length, first_char)
