def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1] and ascending) or (arr[j] < arr[j+1] and not ascending):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
if __name__ == '__main__':
    arr = [3, 3, 2, 10,3, 2, 5]
    new_array = bubble_sort(arr,ascending=True)
    print("Sorted array is:{0}".format(new_array))