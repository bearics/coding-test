from itertools import product

dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]
max_process = 0
max_line = 0


class Maxynos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "x={}, y={}".format(self.x, self.y)


def dfs(maxy_idx, process, line):
  global max_process
  global max_line
  global maxynoses
  global maxynos_num
  global board_map

  if maxy_idx == len(maxynoses):
    # 최대치 업데이트
    if max_process < process:
      max_process = process
      max_line = line
    elif max_process == process:
      max_line = min(max_line, line)
    return

  maxy = maxynoses[maxy_idx]
  x, y = maxy.x, maxy.y

  # 전원이 필요 없는 프로세스
  if x == 0 or x == maxynos_num - 1 or y == 0 or y == maxynos_num - 1:
    dfs(maxy_idx + 1, process + 1, line)
  else:
    # 전원 연결 안하는 경우
    dfs(maxy_idx + 1, process, line)
    # 전원 연결 하는 경우
    for dir_idx in range(4):  # 방향이 가능한지 보고 넘기기
      can_connect = True
      tx, ty = x, y
      nx, ny = dx[dir_idx], dy[dir_idx]
      while (tx + nx >= 0 and tx + nx < maxynos_num) and (ty + ny >= 0 and ty + ny < maxynos_num):
        if board_map[ty + ny ][tx + nx] != 0:
          can_connect = False
          break
        tx, ty = tx + nx, ty + ny
      if can_connect:
        tx, ty = x, y
        count = 0
        while (tx + nx >= 0 and tx + nx < maxynos_num) and (ty + ny >= 0 and ty + ny < maxynos_num):
          tx, ty = tx + nx, ty + ny
          board_map[ty][tx] = 2
          count += 1

        dfs(maxy_idx+1, process+1, line+count)  # 전선 연결하기

        # 초기화 하기
        tx, ty = x, y
        while (tx + nx >= 0 and tx + nx < maxynos_num) and (ty + ny >= 0 and ty + ny < maxynos_num):
          tx, ty = tx + nx, ty + ny
          board_map[ty][tx] = 0


case_num = int(input())
for case_idx in range(case_num):
  maxynos_num = int(input())
  board_map = [[0] * maxynos_num for _ in range(maxynos_num)]
  maxynoses = []
  default_process_count = 0
  max_process = 0
  max_line = 0
  for map_row in range(maxynos_num):
    for map_cell, data in enumerate(list(map(int, input().split()))):
      if data == 1:
        board_map[map_row][map_cell] = data
        maxynoses.append(Maxynos(map_cell, map_row))
  dfs(0, 0, 0)
  print("#{} {}".format(case_idx+1, max_line))
