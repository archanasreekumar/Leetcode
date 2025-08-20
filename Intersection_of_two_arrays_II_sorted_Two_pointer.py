def get_intersec(nums1, nums2):
    i, j = 0, 0
    res = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return res


arr1 = [1, 2, 2, 4, 5]
arr2 = [2, 2, 3, 3]
print(get_intersec(arr1, arr2))
