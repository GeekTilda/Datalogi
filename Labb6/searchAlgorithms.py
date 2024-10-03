def binary_search(arr, target):     # From ChatGPT
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids potential overflow

        if arr[mid] == target:
            return target  # Target found at index mid
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return None  # Target not found

def linear_search(arr, target):     # From ChatGPT
    for index, value in enumerate(arr):
        if value == target:
            return target  # Target found at the current index
    return None  # Target not found

def hash_search(arr, target):       # From ChatGPT
    # Create a hash table (dictionary) from the array
    hash_table = {value : index for index, value in enumerate(arr)}
    
    # Check if the target exists in the hash table
    if target in hash_table:
        return target # hash_table[target]  # Return the index of the target
    return None  # Target not found
