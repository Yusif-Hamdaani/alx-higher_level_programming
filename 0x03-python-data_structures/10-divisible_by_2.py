#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    results = []

    # Loop through each element in the input list
    for num in my_list:
        # Check if the element is divisible by 2
        if num % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    
    # Return the list of results
    return results
