class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        i,j=0,n-1
        
        while i<=j:
            med = (i+j)//2
            print(i, j, med, nums[med])
            if nums[med]==target:
                return med
            elif nums[med]<target:
                i=med+1
            else:
                j=med-1
            
        return -1