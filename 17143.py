from collections import deque as d
from sys import stdin

class Shark:
  def __init__(self, r, c, s, d, z):
    self.r = r
    self.c = c
    self.s = s
    self.d = d
    self.z = z

  def __init__(self, list):
    self.r = list[0]
    self.c = list[1]
    self.s = list[2]
    self.d = list[3]
    self.z = list[4]

  def __str__(self):
    return "{}, {}, {}, {}, {}".format(self.r, self.c, self.s, self.d, self.z)


def reverse_direction(dir):
  if dir is 1:
    return 2
  if dir is 2:
    return 1
  if dir is 3:
    return 4
  if dir is 4:
    return 3


dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]

R, C, M = map(int, input().split())

result_sum = 0
sharks = []
dead_sharks = []
for i in range(M):
  sharks.append(Shark(list(map(int,stdin.readline().strip().split(' ')))))

for man in range(1, C + 1):  # move man
  # input shark in map
  map = [[-1] * (C + 1) for i in range(R + 1)]
  for idx, shark in enumerate(sharks):
    # print(idx)
    # print(shark)
    shark_idx = map[shark.r][shark.c]
    if shark_idx is -1:
      # 상어가 없으면 맵에 상어 배치
      map[shark.r][shark.c] = idx
    else:
      # 만약에 기존에 상어가 있으면 크기 비교 후에 한 명은 사망
      if sharks[shark_idx].z >= shark.z:
        dead_sharks.append(idx)
        # print("Eat {}->{}".format(shark_idx, idx))
      else:
        map[shark.r][shark.c] = idx
        dead_sharks.append(shark_idx)
        # print("Eat {}->{}".format(idx, shark_idx))
  # print("\n map --- man is {}".format(man))
  # for row in map:
  #   print(*row)
  # print("------")
  # for idx, shark in enumerate(sharks):
  #   print(shark)
  # print("------")

  # catch shark
  for row in range(1, R + 1):
    shark_idx = map[row][man]
    if shark_idx is not -1:  # find shark!
      result_sum += sharks[shark_idx].z
      dead_sharks.append(shark_idx)
      # print("Catch shark! in shark({})".format(shark_idx))
      break

  # delete dead sharks
  dead_sharks.sort(reverse=True)
  for dead_shark in dead_sharks:
    sharks.pop(dead_shark)
  dead_sharks.clear()

  # move shark
  for idx, shark in enumerate(sharks):
    if shark.d <= 2:
      for _ in range(shark.s % ((R - 1) * 2)):
        if shark.r == 1 and shark.d == 1:
          shark.d = 2
        if shark.r == R and shark.d == 2:
          shark.d = 1
        shark.r = shark.r + dy[shark.d]
    else:
      for _ in range(shark.s % ((C - 1) * 2)):
        if shark.c == 1 and shark.d == 4:
          shark.d = 3
        if shark.c == C and shark.d == 3:
          shark.d = 4
        shark.c = shark.c + dx[shark.d]

print(result_sum)
