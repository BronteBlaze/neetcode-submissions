class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0

        for i in range(len(nums)):

            j=i
            k=0

            con_array=[nums[i]]

            while k<len(nums):
                if nums[k]==nums[j]+1:
                    con_array.append(nums[k])
                    j=k
                    k=0
                else:
                    k+=1

            print(con_array)

            if length<len(con_array):
                length=len(con_array)
        
        return length
