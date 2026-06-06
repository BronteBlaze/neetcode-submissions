class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = defaultdict(set)
        columns_count = defaultdict(set)
        box_count = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                box = (r//3, c//3)

                if value==".":
                    continue

                if value in row_count[r] or value in columns_count[c] or value in box_count[box]:
                    return False
                
                row_count[r].add(value)
                columns_count[c].add(value)
                box_count[box].add(value)
        
        return True

