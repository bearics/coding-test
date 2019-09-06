def solution(n, computers):
  answer = 0
  networks = []


  for r in range(n):
    for c in range(n):
      if r < c:

      else:
        continue


  return answer


test_case = [
  3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2
  # 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1
]

res = solution(test_case[0], test_case[1])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
