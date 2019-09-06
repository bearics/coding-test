dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up, right, down, left (y, x)

case_num = int(input())

for case_idx in range(1, case_num + 1):
  N = int(input())
  base_map = []
  wormholes = {}
  for idx in range(6, 11):
    wormholes[idx] = []

  for _ in range(N):
    base_map.append(list(map(int, input().split())))

  for r in range(N):
    for c in range(N):
      if base_map[r][c] > 5:  # wormhole
        wormholes[base_map[r][c]].append([r, c])
  # print(wormholes)
  max_score = 0
  count = 0
  for sy in range(N):
    for sx in range(N):
      if base_map[sy][sx] == 0:
        for start_dir in dirs:
          count += 1
          # print("\n start!", count, end=" ")
          score = 0
          # 중복인지 확인
          is_duplicate = False

          if (sy - start_dir[0] >= 0) and (sy - start_dir[0] < N) and (
                  sx - start_dir[1] >= 0) and (sx - start_dir[1] < N):
            if base_map[sy - start_dir[0]][sx - start_dir[1]] == 0:
              is_duplicate = True

          if is_duplicate == True:
            continue

          ny, nx, dy, dx = sy, sx, start_dir[0], start_dir[1]
          while True:
            # print("({}, {}, [{},{}])".format(ny, nx, dy, dx), end=" ")
            is_wall = False
            if (ny + dy >= 0) and (ny + dy < N) and (
                  nx + dx >= 0) and (nx + dx < N):
              next_square = base_map[ny + dy][nx + dx]
            else:  # 벽에 부딪힘
              is_wall = True
              dy, dx = -dy, -dx
              score += 1

            if is_wall == False:  # 벽이 아니면 앞으로 한 칸
              ny, nx = ny + dy, nx + dx

            if next_square == 0:  # 비어 있을때
              score += 0
            elif next_square == 1:
              if (dy == 0 and dx == 1) or (dy == -1 and dx == 0):
                dy, dx = -dy, -dx
              elif dy == 1 and dx == 0:
                dy, dx = 0, 1
              elif dy == 0 and dx == -1:
                dy, dx = -1, 0
              score += 1
            elif next_square == 2:
              if (dy == 0 and dx == 1) or (dy == 1 and dx == 0):
                dy, dx = -dy, -dx
              elif dy == -1 and dx == 0:
                dy, dx = 0, 1
              elif dy == 0 and dx == -1:
                dy, dx = 1, 0
              score += 1
            elif next_square == 3:
              if (dy == 0 and dx == -1) or (dy == 1 and dx == 0):
                dy, dx = -dy, -dx
              elif dy == -1 and dx == 0:
                dy, dx = 0, -1
              elif dy == 0 and dx == 1:
                dy, dx = 1, 0
              score += 1
            elif next_square == 4:
              if (dy == 0 and dx == -1) or (dy == -1 and dx == 0):
                dy, dx = -dy, -dx
              elif dy == 1 and dx == 0:
                dy, dx = 0, -1
              elif dy == 0 and dx == 1:
                dy, dx = -1, 0
              score += 1
            elif next_square == 5:
              dy, dx = -dy, -dx
              score += 1
            elif next_square > 5:  # 웜홀 일때
              wormhole = wormholes[next_square]
              if wormhole[0][0] == ny and wormhole[0][1] == nx:
                ny, nx = wormhole[1]
              else:
                ny, nx = wormhole[0]
            elif next_square == -1:  # 블랙홀
              break

            if ny == sy and nx == sx:  # 초기위치
              break
          max_score = max(max_score, score)
  print("#{} {}".format(case_idx, max_score))