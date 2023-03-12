#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is out of range or negative
    if idx < 0 or idx >= len(my_list):
        # Return the original list
        return my_list

    # Create a new list with all the elements before the index
    new_list = my_list[:idx]

    # Add all the elements after the index to the new list
    new_list.extend(my_list[idx+1:])

    # Return the new list
    return new_list
