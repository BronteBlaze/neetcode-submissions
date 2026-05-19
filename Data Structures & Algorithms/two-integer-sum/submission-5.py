class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      indices = {}
      for i, value in enumerate(nums):
        indices[value] = i
      
      for i, value in enumerate(nums):
        diff = target - value
        if diff in indices.keys() and indices[diff]!=i:
          return [i, indices[diff]]
        
      return []