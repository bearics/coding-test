def solution(citations):
  answer = 0
  citations = sorted(citations)
  for h in reversed(range(0, len(citations)+1)):
    how_many_more = 0
    how_many_less = 0
    for i, c in enumerate(citations):
      if c >= h:
        how_many_more = len(citations) - i
        how_many_less = i
        break
    if how_many_more >= h and how_many_less <= h:
      answer = h
      break

  return answer



test_case = [
  # [3, 0, 6, 1, 5], 3
  [1], 1
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")