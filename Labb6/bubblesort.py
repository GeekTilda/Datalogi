def bubblesort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the process, if no swaps occur, we can stop
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no elements were swapped, break the loop
        if not swapped:
            break
    return arr
