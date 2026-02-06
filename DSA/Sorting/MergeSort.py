# MergeSort using Python..


def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2

    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])

    # Merge
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining
    result.extend(left[i:])
    result.extend(right[j:])

    # Final Return Result(Sort)
    return result

#Test
arr = [3, 2, 6, 8, 1]

sortedArr = MergeSort(arr)
print("The sorted array is", sortedArr)
        
