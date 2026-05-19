class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_copy = nums.copy()
        for num in nums:
            nums_copy.append(num)
        return nums_copy