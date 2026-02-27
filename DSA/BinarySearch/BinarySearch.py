# Binary Search Algorithm Implementation in Python

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:                    # If left becomes greater than right, it means we have exhausted the search space without finding the target, and we can safely conclude that the target is not present in the array.
        mid = (left + right) // 2           # yaha double slash (//) le integer division garxa and decimal part lai ignore garxa. 
        
        if arr[mid] == target:              # Check if the target is present at mid
            return mid
        elif arr[mid] < target:             # If target is greater, ignore the left half
            left = mid + 1
        else:                               # If target is smaller, ignore the right half
            right = mid - 1      
    return 0                               # Target was not found in the array

# Example usage
if __name__ == "__main__":                  # if __name_ is "__main__" le code lai direct run garna milxa, ani aru file bata import garna milxa. matlab code lai reusable banauna milxa. jastai hamile binarySearch function lai aru file bata import garna milxa, ani tyo file ma binarySearch function lai call garna milxa. kasari bhanda--> (from BinarySearch import binarySearch), ani tyo file ma binarySearch function lai call garna milxa. jastai result = binarySearch(sorted_array, target_value) ani tyo file ma sorted_array ra target_value define garna milxa.
    sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    targetValue = 8
    
    result = binarySearch(sortedArray, targetValue)
    
    if result == 0:
        print("Element not found in the array.")
    else:
        print(f"Element found at index: {result}")
        