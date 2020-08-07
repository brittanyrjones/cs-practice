def three_sum_closest(nums, target):

        nums.sort()

        len_nums = len(nums)
        closest = nums[0] + nums[1] + nums[len_nums - 1]
        for i in range(len_nums - 2):
            left = i + 1
            right = len_nums - 1
            while left < right:
                sum_nums = nums[i] + nums[left] + nums[right]
                if sum_nums == target:
                    return target
                else:
                    if abs(sum_nums - target) < abs(closest - target):
                        closest = sum_nums
                    if sum_nums < target:
                        left += 1
                    else:
                        right -= 1

        return closest

print(three_sum_closest([-1,2,1,-4], 2))