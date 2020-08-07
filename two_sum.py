def two_sum(nums, target):
    sums = []
    num_hash = {}

    for i in range(len(nums)):
        sum_pair_number = target - nums[i]
        if sum_pair_number in num_hash:
            print(nums[i],sum_pair_number)
        num_hash[nums[i]] = nums[i]

nums = [4, 5, 1, 8]
target = 9    
  
print(two_sum(nums, target))