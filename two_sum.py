def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    inmap = {}
    for i in range(len(nums)):
        num = nums[i]
        pair = target - num
        if pair in inmap:
            return [inmap[pair], i]
        index_map[num] = i
    return None
 
nums = [1,4,8,2,2,9,16]
target = 11

print(twoSum(nums, target))
