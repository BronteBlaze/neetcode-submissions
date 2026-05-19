class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = dict()
        for i in nums:
            nums_map[i] = nums_map.get(i, 0) + 1
        
        print(nums_map)

        for values in nums_map.values():
            if values>1:
                return True
        
        return False