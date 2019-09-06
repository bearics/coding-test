def solution(m, n, board):
  answer = 0
  base_board = []
  for r in range(m):
    row = []
    for c in range(n):
      row.append(board[r][c])
    base_board.append(row)

  board = [r[:] for r in base_board]

  is_boom = True
  while is_boom:
    is_boom = False
    delete_blocks = []  # (r,c) 2x2 왼쪽 위 좌표
    for r in range(m):
      for c in range(n):
        if r < m - 1 and c < n - 1 and board[r][c] != 0:
          if board[r][c] == board[r][c + 1] and board[r][c] == board[r + 1][c] and board[r][c] == board[r + 1][c + 1]:
            # print("펑 ({}, {})".format(r, c))
            delete_blocks.append((r, c))
            is_boom = True

    # 터진 애들 삭제
    for (r, c) in delete_blocks:
      if board[r][c] != 0:
        answer += 1
        board[r][c] = 0
      if board[r + 1][c] != 0:
        answer += 1
        board[r + 1][c] = 0
      if board[r][c + 1] != 0:
        answer += 1
        board[r][c + 1] = 0
      if board[r + 1][c + 1] != 0:
        answer += 1
        board[r + 1][c + 1] = 0

    for c in range(n):
      one_col = []
      for r in range(m):
        if board[r][c] != 0:
          one_col.append(board[r][c])

      for r in reversed(range(m)):
        if len(one_col) > 0:
          board[r][c] = one_col.pop()
        else:
          board[r][c] = 0

  return answer


test_case = [
  # 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"], 14
  6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"], 15
]

res = solution(test_case[0], test_case[1], test_case[2])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
