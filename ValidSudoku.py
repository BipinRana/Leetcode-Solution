class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        column = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        subset = [[set(),set(),set()],[set(),set(),set()],[set(),set(),set()]]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] not in row[i]:
                        row[i].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in column[j]:
                        column[j].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in subset[i//3][j//3]:
                        subset[i//3][j//3].add(board[i][j])
                    else:
                        return False
                        

        return True


        