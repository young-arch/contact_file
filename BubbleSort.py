def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", my_list)

    bubble_sort(my_list)

    print("Sorted list:", my_list)
