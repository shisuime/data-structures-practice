def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap //= 2

    print("After sort:", arr)  # debug
    arr[:] = remove_duplicates(arr)


def remove_duplicates(arr):
    if not arr:
        return arr

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return arr[:i+1]


if __name__ == "__main__":
    elements=[21,38,29,17,17,4,25,11,11,32,9]
    shell_sort(elements)
    print(elements)