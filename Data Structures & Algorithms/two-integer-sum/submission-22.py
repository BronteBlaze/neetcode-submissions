class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = sorted(enumerate(nums), key=lambda x: x[1])
        i=0
        j=len(indexed)-1
        while i<j:
          if indexed[i][1]+indexed[j][1]<target:
            i+=1
          elif indexed[i][1]+indexed[j][1]>target:
            j-=1
          else:
            return sorted([indexed[i][0], indexed[j][0]])