def has_negatives(a):
    result = []
    # Your code here
    cache = {}
    for n in a:
        if n not in cache:
            cache[n] = n*-1
            if cache[n] in cache and n != 0:
                result.append(abs(cache[n]))
    # print(cache)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
