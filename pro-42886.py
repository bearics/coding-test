def solution(weight):
  answer = 1
  weight = sorted(weight)
  for w in weight:
    if answer < w:
      break
    answer += w


  return answer


test_case = [
  [3, 1, 6, 2, 7, 30, 1], 21
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
