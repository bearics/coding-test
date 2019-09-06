test_case = [["100", "ryan", "music", "2", "1"], ["200", "apeach", "math", "2", "2"], ["300", "tube", "computer", "3", "3"],
             ["400", "con", "computer", "4", "4"], ["500", "muzi", "music", "3", "5"], ["600", "apeach", "music", "2", "6"]]

candidate = []
unique = []
max_col = 0
max_row = 0
ans = []
REL = []


def solve(idx, size):
  global candidate
  global unique
  global ans
  test_uniq = set([])

  if len(candidate) == size:
    print(candidate)
    is_sub = False
    for ans_case in ans:
      if set(ans_case) <= set(candidate):
        is_sub = True
        break
    if is_sub == False:
      for row in REL:
        temp = []
        for cell in candidate:
          temp.append(row[cell])
        test_uniq.add(tuple(temp))
      if len(test_uniq) == max_row:
        ans.append(candidate[:])
        print("suc ", candidate)
    return


  if idx + 1 <= max_col:
    candidate.append(idx)
    solve(idx + 1, size)
    candidate.pop()
    solve(idx + 1, size)


def solution1(relation):
  global max_col, max_row
  global candidate, REL
  REL = relation
  max_col = len(relation[0])
  max_row = len(relation)
  answer = 0
  test_dic = {}

  for size in range(1, max_col+1):
    solve(0, size)

  return len(ans)

def solution(relation):
  answer_list = list()
  print(1<< len(relation[0]))
  for i in range(1, 1 << len(relation[0])):
    tmp_set = set()
    for j in range(len(relation)):
      tmp = ''
      for k in range(len(relation[0])):
        if i & (1 << k):
          tmp += str(relation[j][k])
      tmp_set.add(tmp)

    if len(tmp_set) == len(relation):
      not_duplicate = True
      for num in answer_list:
        if (num & i) == num:
          not_duplicate = False
          break
      if not_duplicate:
        answer_list.append(i)
  return len(answer_list)


if solution(test_case) == 3:
  print("goood")
else:
  print("fail")