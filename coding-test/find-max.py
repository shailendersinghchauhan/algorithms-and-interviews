def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val


arr = [5, 2, 8, 1, 9, 4]
max_val = find_max(arr)
print(max_val)  # Output: 9