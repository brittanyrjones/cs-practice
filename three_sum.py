def three_sum(num):
    sorted_nums = sorted(num) # o(nlog n)?
    output_hash = set()
    for k in range(len(sorted_nums)):
        target = -sorted_nums[k]
        i,j = k+1, len(sorted_nums)-1
        while i < j:
            # print(j)

            sum_two = sorted_nums[i] + sorted_nums[j]
            if sum_two < target:
                i += 1
            elif sum_two > target:
                j -= 1
            else:
                output_hash.add((sorted_nums[k],sorted_nums[i],sorted_nums[j]))
                i += 1
                j -= 1
    return output_hash

print(three_sum([-1, 0, 1, 2, -1, -4]))