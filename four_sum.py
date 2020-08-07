def four_sum(num_array, quad_sum):
    num_hash = {}
    for i in range(len(num_array)-1):
        for j in range(i+1, len(num_array)):
            if num_array[i]+num_array[j] in num_hash: 
                num_hash[num_array[i]+num_array[j]].add((i,j))
            else: 
                num_hash[num_array[i]+num_array[j]] = {(i,j)}
    result = []
    for key in num_hash:
        if -key + quad_sum in num_hash:
            for (i,j) in num_hash[key]:
                for (p,q) in num_hash[-key + quad_sum]:
                    sorted_index = sorted([num_array[i], num_array[j], num_array[p], num_array[q]])
                    if i not in (p, q) and j not in (p, q) and sorted_index not in result:
                        result.append(sorted_index)
    return result

print(four_sum([1,2,3,4,5], 11))