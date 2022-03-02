def first_duplicate(arr):
    num_set = set()

    for i in range(len(arr)):
        if arr[i] in num_set:
            return arr[i]
        else:
            num_set.add(arr[i])

    return "no duplicate value found"


arr = [1, 2, 3, 2, 1]
print("First occurrence of duplicate value is:", first_duplicate(arr))
