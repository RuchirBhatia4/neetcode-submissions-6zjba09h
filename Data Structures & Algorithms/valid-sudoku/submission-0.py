class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            row = [set() for _ in range(9)]
            col = [set() for _ in range(9)]
            boxes = [set() for _ in range(9)]

            for r in range(9):
                for c in range(9):
                    val = board[r][c]
                    if val == '.':
                        continue
                    b = (r // 3) * 3 + (c // 3)
                    if val in row[r] or val in col[c] or val in boxes[b]:
                        return False
                    row[r].add(val)
                    col[c].add(val)
                    boxes[b].add(val)
            return True