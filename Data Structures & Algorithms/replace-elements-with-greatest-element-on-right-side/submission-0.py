class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            large_item = max(arr[i:])
            arr[i-1] = large_item
        
        arr[-1] = -1
        return arr