class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      new_arr = []
      for index, value in enumerate(nums):
        new_arr.append([value, index])
      
      new_arr.sort()
      i,j=0, len(nums)-1
      while i<j:
        if new_arr[i][0]+new_arr[j][0]==target:
          return [min(new_arr[i][1], new_arr[j][1]), max(new_arr[i][1], new_arr[j][1])]
        elif new_arr[i][0]+new_arr[j][0]<target:
          i+=1
        else:
          j-=1

      return []