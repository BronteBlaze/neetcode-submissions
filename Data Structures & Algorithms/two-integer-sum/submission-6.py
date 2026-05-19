class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prev_map = {}

      for i, value in enumerate(nums):
        diff = target - value
        if diff in prev_map:
          return [prev_map[diff], i]
        prev_map[value] = i