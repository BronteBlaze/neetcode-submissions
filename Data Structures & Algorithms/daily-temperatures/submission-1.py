class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        n = len(temperatures)

        for i in range(n):
            first_warmer_index=i

            for j in range(i+1, n):
                if temperatures[j]>temperatures[i]:
                    first_warmer_index = j
                    break

            day = first_warmer_index-i
            result.append(day)
        
        return result