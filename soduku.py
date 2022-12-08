board = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]]

board2 = [
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [7, 1, 3, 0, 2, 4, 8, 5, 6],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [5, 3, 4, 6, 7, 8, 9, 1, 2]]


def valid_solution(board):
    rows, cols = {i: set(board[i]) for i in range(len(board))}, {
        i: set() for i in range(len(board))}
    cells = {i: set() for i in range(len(board))}
    expected = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for b in board:
        for i in range(9):
            cols[i].add(b[i])
            if b[i] not in expected:
                return False
    for i in range(len(board)):
        if i < 3:
            cells[0].update(set(board[i][0:3]))
            cells[1].update(set(board[i][3:6]))
            cells[2].update(set(board[i][6:]))
        elif i < 6:
            cells[3].update(set(board[i][0:3]))
            cells[4].update(set(board[i][3:6]))
            cells[5].update(set(board[i][6:]))
        else:
            cells[6].update(set(board[i][0:3]))
            cells[7].update(set(board[i][3:6]))
            cells[8].update(set(board[i][6:]))
    for i in range(9):
        if len(cells[i]) != 9 or 9 != len(cols[i]) or 9 != len(rows[i]):
            return False
    return True


print(valid_solution(board))
print(valid_solution(board2))
