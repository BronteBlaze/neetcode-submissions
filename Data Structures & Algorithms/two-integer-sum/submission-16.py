class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # Two Pass HashMap
      nums_dict = dict()
      for i, value in enumerate(nums):
        nums_dict[value] = i

      for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_dict and not nums_dict[diff]==i:
          return [i, nums_dict[diff]]
      
      return []