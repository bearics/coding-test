def solution(brown, red):
  answer = []
  for d in range(3, int((brown - 4) / 2) + 10):
    w = int(((brown + 4) / 2) - d)
    # print(w, d)
    if w < d:
      break
    if red == (d -2 ) * (w -2):
      answer.extend([w,d])
      break


  return answer


test_case = [
  # 24, 24, [8, 6]
	8, 1, [3, 3]
]

res = solution(test_case[0], test_case[1])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
