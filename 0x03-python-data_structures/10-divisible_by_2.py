#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the results
    result = []

    # Loop over the elements in the original list and check if they are divisible by 2
    for num in my_list:
        # Append True if the number is divisible by 2, False otherwise
        result.append(num % 2 == 0)

    # Return the result
    return result
