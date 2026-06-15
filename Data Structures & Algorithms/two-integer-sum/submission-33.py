class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        i = 0
        j=len(nums)-1

        while i<j:
          if arr[i][0]+arr[j][0]==target:
            return sorted([arr[i][1],arr[j][1]])
          elif arr[i][0]+arr[j][0]<target:
            i+=1
          else:
            j-=1
        
        return []