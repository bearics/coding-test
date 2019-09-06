for t in range(int(input())):
  M, A = map(int, input().split())
  moveA = [0]
  moveA += list(map(int, input().split()))

  moveB = [0]
  moveB += list(map(int, input().split()))

  dirs = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
  m = [[list() for _ in range(10)] for _ in range(10)]

  APs = []
  BC_i = 1
  for _ in range(A):
    c, r, coverage, performance = map(int, input().split())
    # install BC
    r -= 1
    c -= 1
    for i in range(10):
      for j in range(10):
        if abs(i - r) + abs(j - c) <= coverage:
          m[i][j].append((performance, BC_i))
    BC_i += 1

  answer = 0
  Ar, Ac = 0, 0
  Br, Bc = 9, 9

  for a, b in zip(moveA, moveB):
    Adt, Bdt = dirs[a], dirs[b]

    Ar += Adt[0]
    Ac += Adt[1]

    Br += Bdt[0]
    Bc += Bdt[1]

    Ap, Ai = max(m[Ar][Ac]) if m[Ar][Ac] else (0, 0)
    Bp, Bi = max(m[Br][Bc]) if m[Br][Bc] else (0, 0)

    if Ai == Bi:  # 같은 BC에 있음. 나눠가져야 함
      d = {}
      for perform, i in m[Ar][Ac]:
        d[i] = perform

      for perform, i in m[Br][Bc]:
        d[i] = perform

      result = sorted(d.values(), reverse=True)
      if len(result) == 1:
        answer += Ap
      elif len(result) == 0:
        answer += 0
      else:
        answer += (result[0] + result[1])
    else:  # 두 사람이 다른 BC에 있음.
      answer += (Ap + Bp)

  print("#%d %d" % (t + 1, answer))