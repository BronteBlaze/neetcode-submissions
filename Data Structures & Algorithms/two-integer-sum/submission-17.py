class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # Two Pass HashMap
      nums_dict = dict()

      for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_dict and not nums_dict[diff]==i:
          return [nums_dict[diff], i]
        nums_dict[nums[i]] = i
      
      return []

      # TimeComplexity: o(n)
      # SpaceComplexity: o(n)