class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            med = (left+right)//2

            if nums[med]==target:
                return med
            elif nums[left]<=nums[med]:
                if nums[left]<=target<nums[med]:
                    right=med-1
                else:
                    left=med+1
            elif nums[right]>=nums[med]:
                if nums[right]>=target>nums[med]:
                    left=med+1
                else:
                    right=med-1
        
        return -1