def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Inläsning av data
# Läs in den första raden som en lista av sorterade strängar
sorted_list = input().split()

# Läs in söksträngarna, en per rad tills vi får '#'
search_strings = []
while True:
    search_str = input().strip()
    if search_str == '#':
        break
    search_strings.append(search_str)

# Utför binärsökning för varje söksträng och skriv ut resultatet
for s in search_strings:
    result = binary_search(sorted_list, s)
    if result:
        print(result)
    else:
        print("None")
