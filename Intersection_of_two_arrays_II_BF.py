def get_intersec(arr1, arr2):
    out = []
    arr2_copy = arr2
    for num in arr1:
        if num in arr2:
            out.append(num)
            arr2_copy.remove(num)
    return out


arr1 = [1, 2, 2, 4, 5]
arr2 = [2]
print(get_intersec(arr1, arr2))
