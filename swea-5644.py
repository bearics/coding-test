dirs = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]  # [y, x]

T = int(input())

for case_idx in range(1, T + 1):
  M, A = list(map(int, input().split()))
  moves, positions = [], [[0, 0], [9, 9]]  # [y, x]
  answer = 0
  moves.append(list(map(int, input().split())))
  moves.append(list(map(int, input().split())))
  time = len(moves[0])
  aps = []
  base_map = [[[] for _ in range(10)] for _ in range(10)]

  for _ in range(A):
    ap = list(map(int, input().split()))  # x, y, c(범위), p
    ap[0], ap[1] = ap[0] - 1, ap[1] - 1
    aps.append(ap)

  for idx, ap in enumerate(aps):
    x, y, c, p = ap
    for ir in range(-c, c + 1):
      for ic in range(-c, c + 1):
        if abs(ir) + abs(ic) < c + 1:
          if ap[1] + ir >= 0 and ap[1] + ir < 10 and ap[0] + ic >= 0 and ap[0] + ic < 10:
            base_map[ap[1] + ir][ap[0] + ic].append(idx)

  # for r in base_map:
  #   print(*r)

  for t in range(time + 1):
    # 가까운 ap로 부터 충전
    possible_aps = []
    for man in range(2):
      my, mx = positions[man]  # 사람 위치
      possible_aps.append(base_map[my][mx])

    # if t == 47:
    #   print("dd")

    a_possible, b_possible = possible_aps
    common_possible = set(a_possible) & set(b_possible)
    a_only_possible = set(a_possible) - set(common_possible)
    b_only_possible = set(b_possible) - set(common_possible)
    all_possible = set(a_possible) | set(b_possible)

    all_possible = sorted(all_possible, key=lambda i: aps[i][3])
    a_only_possible = sorted(a_only_possible, key=lambda i: aps[i][3])
    b_only_possible = sorted(b_only_possible, key=lambda i: aps[i][3])
    common_possible = sorted(common_possible, key=lambda i: aps[i][3])
    sum = 0
    max_idxs = [0] * 2
    try:
      max_idxs[0] = a_only_possible.pop()
    except IndexError:
      max_idxs[0] = -1
    try:
      max_idxs[1] = b_only_possible.pop()
    except IndexError:
      max_idxs[1] = -1
    max_idxs += common_possible


    ranked_r = []
    for max_idx in max_idxs:
      if max_idx != -1:
        ranked_r.append(max_idx)

    ranked_r = sorted(ranked_r, key=lambda i: aps[i][3])
    try:
      for _ in range(2):
        sum += aps[ranked_r.pop()][3]
    except IndexError:
      pass

    answer += sum

    # 이동
    for man in range(2):
      try:
        dy, dx = dirs[moves[man][t]]
        my, mx = positions[man]
        positions[man] = [my + dy, mx + dx]
      except IndexError:
        pass

  print("#{} {}".format(case_idx, answer))
