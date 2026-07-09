class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n-1

        while left<=right:
            med = (left+right)//2

            row = med//n
            column = med%n

            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                left=med+1
            else:
                right=med-1
        
        return False

