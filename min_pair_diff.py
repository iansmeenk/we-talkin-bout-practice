"""
Given two arrays of integers that:
    - Are of equal length
    - Are unsorted
Return:
    The smallest possible absolute difference between any value in each array

Example:
    a1 = [3, 7, 72, 800]
    a2 = [45, 65, 1000, -20]
    answer = abs(72 - 65) = 7
"""

def brute_force(array1, array2):
    """
    Idea: 
        Loop through every possible combo and find the lowest value
    Complexity:
        O(n^2)
    """
    total_ops = 0
    min_diff = None
    for val1 in array1:
        for val2 in array2:
            total_ops = total_ops + 1
            abs_diff = abs(val1 - val2)
            if min_diff is None or abs_diff < min_diff:
                min_diff = abs_diff
    
    return min_diff, total_ops


def sort_and_point(array1, array2):
    """
    Idea:
        Sort each array (ascending) and set pointers at the first value of each.
        Take the difference between each of the pointed values.
        Test it with the lowest recorded value.
        Move the pointer pointing to the lower value up one.
    Complexity:
        Sorting: O(m log(m) + n log(n))
        Minding min difference: O(m + n)
    """
    total_ops = 0
    array1_sorted = sorted(array1)
    array2_sorted = sorted(array2)

    pointer1 = 0
    pointer2 = 0
    min_diff = None
    
    while pointer1 < len(array1_sorted) and pointer2 < len(array2_sorted):
        total_ops = total_ops + 1
        value1 = array1_sorted[pointer1]
        value2 = array2_sorted[pointer2]

        abs_diff = abs(value1 - value2)
        
        if abs_diff == 0:
            return 0
        elif min_diff is None or abs_diff < min_diff:
            min_diff = abs_diff
        
        if value1 < value2:
            pointer1 = pointer1 + 1
        elif value1 > value2:
            pointer2 = pointer2 + 1
    
    return min_diff, total_ops



if __name__=='__main__':
    a1 = [3, 7, 72, 800]
    a2 = [45, 65, 1000, -20]
    bf_result, bf_operations = brute_force(a1, a2)
    sp_result, sp_operations = sort_and_point(a1, a2)

    print()
    print("Brute Force:")
    print("Result:", bf_result, "\tNumber of Operations:", bf_operations)
    print()
    
    print("Sort and Point:")
    print("Result:", sp_result, "\tNumber of Operations:", sp_operations)
    print()