#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Initialize the maximum to the first element of the list
    max_value = my_list[0]

    # Loop over the rest of the elements and update the maximum if necessary
    for num in my_list[1:]:
        if num > max_value:
            max_value = num

    # Return the maximum
    return max_value
