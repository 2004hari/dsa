def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Choose a pivot (we'll use the first element)
    pivot = arr[0]

    # Step 2: Separate the array into two parts
    # - Elements smaller than or equal to the pivot
    # - Elements greater than the pivot
    less_than_pivot = []
    greater_than_pivot = []

    for i in arr[1:]:  # Start from the second element
        if i <= pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)

    # Step 3: Recursively sort the two parts and combine
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = quick_sort(unsorted_list)
print("Sorted List:", sorted_list)
