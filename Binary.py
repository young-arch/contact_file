def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found, return its index
        elif mid_value < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    sorted_list = [11, 22, 25, 34, 64, 90]
    target_value = 34

    result = binary_search(sorted_list, target_value)

    if result != -1:
        print(f"Element {target_value} found at index {result}.")
    else:
        print(f"Element {target_value} not found in the list.")
