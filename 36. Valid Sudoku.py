#Solution 1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols= collections.defaultdict(list)
        rows=collections.defaultdict(list)
        squares=collections.defaultdict(list)

        for i in range(0,9):
            for j in range(0,9):
                ch= board[i][j]
                if ch==".":
                    continue
                if (ch in rows[i] or ch in cols[j] or ch in squares[(i//3,j//3)]):
                    return False
                rows[i].append(ch)
                cols[j].append(ch)
                squares[(i//3,j//3)].append(ch)
        
        return True

#Solution 2
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp=[]
        for lst in board:
            for l in lst:
                if l != ".":
                    if l in temp:
                        return False
                    temp.append(l)
            temp.clear()
        
        for i in range(0,9):
            for j in range(0,9):
                l=board[j][i]
                if l!=".":
                    print(l)
                    if l in temp:
                        return False
                    temp.append(l)
            temp.clear()

        
        for i in range(0,3):
            for j in range(0,3):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()

        for i in range(0,3):
            for j in range(3,6):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()

        for i in range(0,3):
            for j in range(6,9):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()

        for i in range(3,6):
            for j in range(0,3):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()

        for i in range(3,6):
            for j in range(3,6):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()

        for i in range(3,6):
            for j in range(6,9):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()


        for i in range(6,9):
            for j in range(0,3):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()

        for i in range(6,9):
            for j in range(3,6):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()


        for i in range(6,9):
            for j in range(6,9):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()


        for i in range(0,3):
            for j in range(0,3):
                l=board[i][j]
                if l!=".":
                    if l in temp:
                        return False
                temp.append(l)
        temp.clear()

        return True