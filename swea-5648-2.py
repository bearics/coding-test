def solve():
  N = int(input())
  nucs = [list(map(int, input().split())) for n in range(N)]

  candidate = []  # 충돌 가능한 경우들
  # 원자 2개 combination
  for nuc1_n in range(N - 1):
    for nuc2_n in range(nuc1_n + 1, N):  # (0, 1), ..., (0, N - 1), ..., (N - 2, N - 1)
      # 충돌 가능한 경우는 같은 x값을 갖고 수직으로 움직이거나
      # 같은 y값을 갖고 수평으로 움직이거나
      # 어쩌다 직각으로 충돌하거나
      dx = nucs[nuc1_n][0] - nucs[nuc2_n][0]
      dy = nucs[nuc1_n][1] - nucs[nuc2_n][1]
      d1, d2 = nucs[nuc1_n][2], nucs[nuc2_n][2]

      if dx == 0:  # x값이 같을 때
        if dy > 0:  # 첫번째 원자가 위쪽에 있다면
          if d1 == 1 and d2 == 0:  # 첫번째 원자는 아래로, 두번째 원자는 위로
            candidate.append([nuc1_n, nuc2_n, abs(dy) / 2])
        else:  # 첫번째 원자가 아래에 있다면
          if d1 == 0 and d2 == 1:  # 첫번쨰 원자는 위로, 두번째 원자는 아래로
            candidate.append([nuc1_n, nuc2_n, abs(dy) / 2])

      elif dy == 0:  # y값이 같을 때
        if dx > 0:  # 첫번째 원자가 오른쪽에 있다면
          if d1 == 2 and d2 == 3:  # 첫번째 원자는 왼쪽, 두번쨰 원자는 오른쪽
            candidate.append([nuc1_n, nuc2_n, abs(dx) / 2])
        else:  # 첫번째 원자가 왼쪽에 있다면
          if d1 == 3 and d2 == 2:  # 첫번째 원자는 오른쪽, 두번째 원자는 왼쪽
            candidate.append([nuc1_n, nuc2_n, abs(dx) / 2])

      elif dx == dy:  # +45도
        if dx < 0:  # 우, 하 또는 상, 좌 조합일 때 충돌
          if (d1 == 3 and d2 == 1) or (d1 == 0 and d2 == 2):
            candidate.append([nuc1_n, nuc2_n, abs(dx)])
        else:  # 좌, 상 또는 하, 우 조합일 때 충돌
          if (d1 == 2 and d2 == 0) or (d1 == 1 and d2 == 3):
            candidate.append([nuc1_n, nuc2_n, abs(dx)])

      elif dx == -dy:  # -45도
        if dx < 0:  # 우, 상 또는 하, 좌 조합일 때 충돌
          if (d1 == 3 and d2 == 0) or (d1 == 1 and d2 == 2):
            candidate.append([nuc1_n, nuc2_n, abs(dx)])
        else:  # 좌, 하 또는 상, 우 조합일 때 충돌
          if (d1 == 2 and d2 == 1) or (d1 == 0 and d2 == 3):
            candidate.append([nuc1_n, nuc2_n, abs(dx)])

      else:  # 충돌 가능성 없는 조합
        pass
  # 충돌 가능성 있는 조합 선정 완료
  # 충돌 시간을 기준으로 정렬
  candidate = sorted(candidate, key=lambda x: x[2], reverse=True)
  existing = [True] * len(nucs)
  total_energy = 0

  # 동시에 여러 개(특히 홀수 개) 만나는 경우를 고려해야 함
  # 같은 시간에 충돌하는 원자를 모두 모은다
  while candidate:
    loop_time = candidate[-1][2]
    temp = []
    try:
      while loop_time == candidate[-1][2]:
        n1, n2, time = candidate.pop()
        # 예를 들어 첫 루프에서 1, 2 두번쨰 루프에서 2, 3이 충돌한다면 모두 1, 2, 3이 충돌하는 것
        # 공유되는 원자가 있는 것들을 하나의 충돌 이벤트로 묶어야 함
        # [[1, 2, 3], [7, 16]] 이런 식으로?
        if existing[n1] == False or existing[n2] == False:
          continue

        flag = False
        for cmb in temp:  # temp에는 나오는 조합을 저장. 원자가 겹치는 것을 하나의 리스트로 묶어서 리스트로 저장한다.
          if n1 in cmb or n2 in cmb:  # 이미 있는 경우에 추가하고 (나중에 set으로 겹치는 것 제거)
            cmb += [n1, n2]
            flag == True
          # 없으면.... 끝까지 없으면 새 리스트를 추가해야 하는데

        if flag == False:
          temp.append([n1, n2])
    except:
      pass
    # 충돌 시간이 같은 원자들을 리스트에 묶어둠
    temp1 = []
    for lst in temp:
      temp1 += lst
    temp1 = set(temp1)
    for nuc in temp1:
      total_energy += nucs[nuc][3]
      existing[nuc] = False

  return total_energy


T = int(input())
for tc in range(1, T + 1):
  soln = solve()
  print("#{} {}".format(tc, soln))