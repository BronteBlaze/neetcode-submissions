class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        nums_list = []

        for i in range(len(nums)):
                j=i+1
                k=len(nums)-1

                target=0-nums[i]


                while j<k:
                    if nums[j]+nums[k]==target and [nums[i], nums[j], nums[k]] not in nums_list:
                        nums_list.append([nums[i], nums[j], nums[k]])
                        j+=1
                        k-=1
                    elif nums[j]+nums[k]<target:
                        j+=1
                    else:
                        k-=1

        print(nums_list) 

        return nums_list
