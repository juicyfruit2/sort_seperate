#Considering the given list [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100], if the list is sorted, binary search would be an appropriate choice due to its efficiency for sorted lists.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


# Example usage
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

target_number = 9

# Perform binary search
index = binary_search(sorted(numbers), target_number)

# Check if the target number was found
if index != -1:
    print(f"The number {target_number} was found at index {index}.")
else:
    print(f"The number {target_number} was not found in the list.")

# In this case, the Binary Search algorithm is a good choice because it requires a sorted list. Sorting the list first allows us to leverage the efficiency of Binary Search, which has a time complexity of O(log n) (where n is the size of the sorted list). This algorithm is particularly advantageous for large lists as it significantly reduces the number of comparisons needed to find the target number compared to linear search.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Example usage
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Perform insertion sort
insertion_sort(numbers)

# Print the sorted array
print("Sorted array:", numbers)


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Example usage
numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_number = 9

# Perform interpolation search
index = interpolation_search(sorted(numbers), target_number)

# Check if the target number was found
if index != -1:
    print(f"The number {target_number} was found at index {index}.")
else:
    print(f"The number {target_number} was not found in the list.")


# One real-world application where Interpolation Search can be useful is in searching for elements in large, sorted datasets with uniformly distributed values. For example, it can be used in database systems to search for records based on a specific attribute value. 


