def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    for i in weights:
        if i not in cache:
            cache[i] = limit - i
        else:
            cache[f'{i+1}'] = limit - i

    for i in cache:
        for j in cache:
            if cache[i] + cache[j] == limit and i != j:
                return(list(cache.keys()).index(j), list(cache.keys()).index(i))
    else:
        return None
