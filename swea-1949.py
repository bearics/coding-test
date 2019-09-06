dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def dfs(r, c, dist, use_K):
  global base_map
  global max_distance

  max_distance = max(max_distance, dist)
  now_height = base_map[r][c]
  base_map[r][c] = -1

  # for row in base_map:
  #   print(*row)

  for dx, dy in dirs:
    nx, ny = c + dx, r + dy
    if (nx < 0 or nx >= N) or (ny < 0 or ny >= N):  # 범위 밖
      continue
    if base_map[ny][nx] == -1:
      continue
    if now_height > base_map[ny][nx]:  # 다음 봉우리가 낮음
      dfs(ny, nx, dist + 1, use_K)
    else:  # 다음 봉우리가 같거나 높음
      if use_K:  # K를 썼으면 끝.
        continue
      else:  # 봉우리 깎을 수 있음
        if now_height > base_map[ny][nx] - K:  # 깎으면 되니?
          next_height = base_map[ny][nx]
          base_map[ny][nx] = now_height - 1
          dfs(ny, nx, dist + 1, True)
          base_map[ny][nx] = next_height
        else:
          continue

  base_map[r][c] = now_height


case_num = int(input())
for case_idx in range(case_num):
  # input
  N, K = map(int, input().split())
  base_map = []
  for r in range(N):
    base_map.append(list(map(int, input().split())))
  # print(base_map)

  # find higest
  highest_height = 0
  highest_pos = []  # [[r,c], ... ]
  for r in range(N):
    for c in range(N):
      if base_map[r][c] >= highest_height:
        highest_height = base_map[r][c]
  for r in range(N):
    for c in range(N):
      if base_map[r][c] == highest_height:
        highest_pos.append([r,c])


  # check highest pos
  max_distance = 0
  for hr, hc in highest_pos:
    dfs(hr, hc, 1, False)

  print("#{} {}".format(case_idx + 1, max_distance))
