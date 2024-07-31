def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in nums[:i] or remain in nums[i+1:]:
            nums.pop(i)
            return [i, nums.index(remain) + 1]