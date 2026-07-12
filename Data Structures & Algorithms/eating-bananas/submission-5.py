class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)

        min_hour = 0

        while i<=j:
            med = (i+j)//2       

            total_hours = 0
            
            for k in range(len(piles)):
                total_hours += math.ceil(piles[k]/med)
            
            if total_hours<=h:
                min_hour = med
                j=med-1
            else:
                i=med+1
        
        return min_hour
        

