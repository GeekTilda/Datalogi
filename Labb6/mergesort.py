def mergesort(data):
    if len(data) > 1:
        middle = len(data)//2
        leftHalf = data[:middle]
        rightHalf = data[middle:]

        mergesort(leftHalf)
        mergesort(rightHalf)

        i, j, k = 0, 0, 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                data[k] = leftHalf[i]
                i += 1
            else:
                data[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            data[k] = leftHalf[i]
            i += 1
            k += 1
        
        while j < len(rightHalf):
            data[k] = rightHalf[j]
            j += 1
            k += 1