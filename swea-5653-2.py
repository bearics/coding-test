from collections import deque


def bfs(K, height, width):
  global stem_cells
  time = 1
  while time <= K:
    len_q = len(stem_cells)
    depth_cache = {}
    for _ in range(len_q):
      y, x, life, is_act = stem_cells.popleft()
      if is_act:
        # append 조건, 죽지 않았을 경우
        for ny, nx in ((y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)):
          if not life_map[ny][nx]:
            if depth_cache.get((ny, nx), 0):
              if depth_cache[(ny, nx)] < life_map[y][x]:
                depth_cache[(ny, nx)] = life_map[y][x]  # depth_cache[(ny,nx)]=life
            else:
              depth_cache[(ny, nx)] = life_map[y][x]
        if life == 1:
          life_map[y][x] = -1
        else:
          stem_cells.append([y, x, life - 1, is_act])
      else:
        if life == 1:
          stem_cells.append([y, x, life_map[y][x], True])
        else:
          stem_cells.append([y, x, life - 1, False])
    # print(depth_cache)
    for k, v in depth_cache.items():
      y, x = k
      stem_cells.append([y, x, v, False])
      life_map[y][x] = v
    time += 1
  return len(stem_cells)


for tc in range(1, int(input()) + 1):
  N, M, K = map(int, input().split())
  extra = K // 2 + 1
  life_map = [[0 for _ in range(2 * extra + M)] for _ in range(extra)]
  for _ in range(N):
    life_map.append([0 for _ in range(extra)] + list(map(int, input().split())) + [0 for _ in range(extra)])
  for _ in range(extra):
    life_map.append([0 for _ in range(2 * extra + M)])
  stem_cells = deque([])

  for y, row in enumerate(life_map[1:-1]):
    for x, v in enumerate(row):
      if v:
        stem_cells.append([y + 1, x, v, False])
  result = bfs(K, len(life_map), len(life_map[0]))
  print("#%d %d" % (tc, result))
