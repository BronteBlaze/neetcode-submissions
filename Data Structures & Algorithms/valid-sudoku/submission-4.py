class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        column_map = defaultdict(set)
        box_map = defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                element = board[r][c]

                if element==".":
                    continue
                
                box = (r//3, c//3)

                if element in row_map[r] or element in column_map[c] or element in box_map[box]:
                    return False
                
                row_map[r].add(element)
                column_map[c].add(element)
                box_map[box].add(element)
        

        return True
