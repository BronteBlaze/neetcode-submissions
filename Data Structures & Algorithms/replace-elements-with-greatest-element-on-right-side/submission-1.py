class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            right_max = -1
            for j in range(i+1, n):
                right_max = max(arr[j], right_max)
            ans[i] = right_max
        return ans