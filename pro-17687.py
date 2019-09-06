def solution(n, t, m, p):
  answer = ''
  num_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

  paper = ''
  num = 0
  idx = 0
  while len(paper) <= m * t + p:
    share, rest = num, num
    temp_str = ''
    while share >= n:
      share, rest = int(share / n), share % n
      temp_str = num_arr[rest] + temp_str

    temp_str = num_arr[share] + temp_str
    paper += temp_str
    num += 1

  for idx in range(t):
    answer += paper[((idx*m) + p) -1]

  # print(paper)
  return answer


test_case = [
  # 16, 16, 2, 1, "02468ACE11111111"
2, 4, 2, 1, "0111"
]

res = solution(test_case[0], test_case[1], test_case[2], test_case[3])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
