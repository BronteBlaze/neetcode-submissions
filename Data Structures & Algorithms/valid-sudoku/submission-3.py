class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_map = defaultdict(set)

        for r in range(9):
            for c in range(9):
                
                element = board[r][c]

                if element==".":
                    continue
                
                box = (r//3, c//3)

                row_key = ("row", r)
                column_key = ("column", c)
                box_key = ("box", box)

                if element in board_map[row_key] or element in board_map[column_key] or element in board_map[box_key]:
                    return False
                
                board_map[row_key].add(element)
                board_map[column_key].add(element)
                board_map[box_key].add(element)
        
        return True