def kth_smallest(nums, k): 
  
    # Sort the given array  
    nums.sort() 
  
    # Return k'th element in the  
    # sorted array  
    return nums[k-1] 
  
nums = [12, 3, 5, 7, 19] 
k = 2
print(kth_smallest(nums, k)) 