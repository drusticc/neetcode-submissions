class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        boxes = defaultdict(list)
        row = 0
        box = 0
        column = 0

        for r in board:
            row += 1
            print("row: " + str(row))
            column = 0
            box = 0
            for n in r:
                column += 1
                print("column: " + str(column))
                if column % 3 == 1:
                    box += 1
                    box = ((row - 1) // 3) * 3 + ((column - 1) // 3) + 1
                print("box: " + str(box))

                if n == ".":
                    continue
                if n in rows[row]:
                    return False
                if n in columns[column]:
                    return False
                if n in boxes[box]:
                    return False
                rows[row].append(n)
                columns[column].append(n)
                boxes[box].append(n)
        return True


    