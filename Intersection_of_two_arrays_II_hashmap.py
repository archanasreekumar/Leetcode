def get_intersec(arr1, arr2):
    freq = {}
    out = []
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1

    for num in arr2:
        if num in freq and freq[num] > 0:
            out.append(num)
            freq[num] -= 1
    return out


arr1 = [1, 2, 2, 4, 5]
arr2 = [2, 3, 3, 2]
print(get_intersec(arr1, arr2))
