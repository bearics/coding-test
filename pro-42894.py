def get_minmax(pos_list):
  min_pos, max_pos = [100, 100], [0, 0]  # [r,c]
  for pos in pos_list:
    min_pos = [min(pos[0], min_pos[0]), min(pos[1], min_pos[1])]
    max_pos = [max(pos[0], max_pos[0]), max(pos[1], max_pos[1])]
  return [min_pos, max_pos]


def solution(board):
  answer = 0
  max_row, max_col = len(board), len(board[0])
  is_boom = True
  blocks_pos = {}
  for r in range(max_row):
    for c in range(max_col):
      if board[r][c] != 0:
        block_idx = board[r][c]
        if not block_idx in blocks_pos:
          blocks_pos[block_idx] = []
        blocks_pos[block_idx].append((r, c))

  blocks = {}
  for block_idx in blocks_pos:
    blocks[block_idx] = get_minmax(blocks_pos[block_idx])

  is_boom = True
  while is_boom:
    is_boom = False
    # print(blocks)
    delete_block_idx = -1
    for block_idx in blocks:
      min_pos, max_pos = blocks[block_idx]  # [r, c]
      count = 0
      for r in range(max_pos[0], min_pos[0]-1, -1):
        for c in range(min_pos[1], max_pos[1]+1):
          if board[r][c] == 0:
            can_fill = True
            for up in range(1, r+1):
              if board[r-up][c] != 0:
                can_fill = False
                break
            if can_fill == True:
              count += 1
      if count == 2:  # 블록 삭제
        for r, c in blocks_pos[block_idx]:
          board[r][c] = 0
        delete_block_idx = block_idx
        # print("펑({})".format(block_idx))
        answer +=1
        is_boom = True
        break
    if delete_block_idx != -1:
      del blocks[delete_block_idx]


  return answer


test_case = [
  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
   [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
   [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]],
  2  # result
]

res = solution(test_case[0])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
