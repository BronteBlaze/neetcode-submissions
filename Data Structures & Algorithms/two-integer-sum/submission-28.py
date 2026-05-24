class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      sum_map = defaultdict(int)

      for index, num in enumerate(nums):
        diff = target - num
        if diff in sum_map:
          return [sum_map[diff], index]
        sum_map[num] = index