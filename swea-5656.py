dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # R D L U, [X, Y]


def sol(n):
  # global debugggg
  # debugggg += 1
  # print(debugggg)
  global base_map
  # if debugggg == 28:
  #   print("stop")
  if len(n) >= N:
    count = 0
    global min_count
    for rr in range(H):
      for cc in range(W):
        if base_map[rr][cc] != 0:
          count += 1
    min_count = min(min_count, count)
    # if n[0] == 2 and n[1] ==2 and n[2] == 6:
    #   print("here!!")
    # print(n)
    # for _r in base_map:
    #   print(*_r)
    return
  # print(n, end=" ")
  for c in range(W):
    # 부술 벽돌이 있는지 확인
    have_brick = False
    broken_bricks = []
    for r in range(H):
      if base_map[r][c] != 0:
        broken_bricks.append([r, c])
        break

    prev_map = [row[:] for row in base_map]

    # c열에는 벽돌이 없어서 끝
    if len(broken_bricks) == 0:
      continue

    # c열에 깰 벽돌이 있음
    broken_map = [[0] * W for _ in range(H)]
    while broken_bricks:
      br, bc = broken_bricks.pop(0)
      count = base_map[br][bc]
      for dx, dy in dirs:
        broken_map[br][bc] = 1
        base_map[br][bc] = -1
        if count == 1:
          break
        for idx in range(1, count):
          if ((br + (idx * dy)) < 0 or (br + (idx * dy)) >= H) or ((bc + (idx * dx)) < 0 or (bc + (idx * dx)) >= W):
            continue
          else:
            if base_map[br + (idx * dy)][bc + (idx * dx)] > 0 and broken_map[br + (idx * dy)][bc + (idx * dx)] == 0:
              broken_bricks.append([br + (idx * dy), bc + (idx * dx)])
              broken_map[br + (idx * dy)][bc + (idx * dx)] = 1

    # 벽돌 제거
    for rr in range(H):
      for cc in range(W):
        if broken_map[rr][cc] == 1:
          base_map[rr][cc] = 0

    # 벽돌 정리
    for cc in range(W):
      temp = []
      for rr in range(H):
        if base_map[rr][cc] != 0:
          temp.append(base_map[rr][cc])
        base_map[rr][cc] = 0
      for r_idx in range(len(temp)):
        base_map[H - r_idx - 1][cc] = temp[len(temp) - r_idx - 1]

    # print("n:{} c:{}".format(n, c), end='  ')
    n.append(c)
    sol(n)
    n.pop()
    base_map = [_[:] for _ in prev_map]


T = int(input())
for case_idx in range(T):
  N, W, H = map(int, input().split())
  # print(N, W, H)
  base_map = []

  for row in range(H):
    base_map.append(list(map(int, input().split())))
  min_count = 999999
  debugggg = 0
  sol([])
  if min_count is 999999:
    min_count = 0
  print("#{} {}".format(case_idx + 1, min_count))
