for case_idx in range(1, int(input())+1):
  answer = 0
  N, X = list(map(int, input().split()))
  base_map = [[], []]

  for r in range(N):
    base_map[0].append([])
    for d in list(map(int, input().split())):
      base_map[0][r].append([d, 0])

  base_map[1] = [[[] for _ in range(N)] for _ in range(N)]
  for r in range(N):
    for c in range(N):
      base_map[1][r][c] = [base_map[0][c][r][0], 0]
  for map_idx in range(2):
    r = 0
    while r < N:
      # if r == 1:
      #   print("dd")
      is_suc = True
      c = 0
      while c < N - 1:
        now = base_map[map_idx][r][c][0]
        next = base_map[map_idx][r][c + 1][0]

        if now == next:  # 평평
          c += 1
        elif now + 1 == next:  # 올라감
          is_ok = True
          for i in range(X):
            if c - i >= 0:
              if base_map[map_idx][r][c - i][0] != now or base_map[map_idx][r][c - i][
                1] == 1:  # 이미 경사로 있거나, X만큼 현재 높이 만큼 유지 안될때
                is_ok = False
                break
            else:
              is_ok = False
              break
          if is_ok == True:
            for i in range(X):
              base_map[map_idx][r][c - i][1] = 1
            c += 1
          else:
            is_suc = False
            break;  # 이번 라인 망했어요
        elif now - 1 == next:
          is_ok = True
          for i in range(1, X + 1):
            if c + i < N:
              if base_map[map_idx][r][c + i][0] != next:
                is_ok = False
                break
            else:
              is_ok = False
              break
          if is_ok == True:
            for i in range(1, X + 1):
              base_map[map_idx][r][c + i][1] = 1
            c += X
          else:
            is_suc = False
            break;  # 이번 라인 망했어요
        else:
          is_suc = False
          break
      if is_suc == True:
        # print(r)
        answer += 1
      r += 1

  print("#{} {}".format(case_idx, answer))
