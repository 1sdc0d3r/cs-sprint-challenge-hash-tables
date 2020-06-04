def intersection(arrays):
    nums = {}
    result = []
    for arr in arrays:
        for n in arr:
            if n not in nums:
                nums[n] = 1
            else:
                nums[n] += 1
    for n in nums:
        if nums[n] > 1:
            result.append(n)

    return result


if __name__ == "__main__":
    arrays = [list(range(10, 20)), [1, 2, 3], [1, 2, 3]]

    #   arrays.appendlist(range(10, 20)), [1, 2, 3])
    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
