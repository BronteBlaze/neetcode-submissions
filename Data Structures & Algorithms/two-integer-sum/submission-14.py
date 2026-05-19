class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      values = []
      for i, value in enumerate(nums):
        values.append((value, i))

      values.sort(key=lambda x: x[0])

      i,j=0, len(values)-1
      while i<j:
        if values[i][0]+values[j][0]<target:
          i+=1
        elif values[i][0]+values[j][0]>target:
          j-=1
        else:
          return sorted([values[i][1], values[j][1]])
      
      return []