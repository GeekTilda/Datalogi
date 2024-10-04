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

class HashTable:    # From ChatGPT.
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table."""
        self.table[key] = value

    def search(self, key):
        """Searches for a key in the hash table and returns its value if found, else None."""
        return self.table.get(key, None)

    def delete(self, key):
        """Deletes a key-value pair from the hash table."""
        if key in self.table:
            del self.table[key]
