def solution(answers):
  answer = []
  omrs = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ]
  man_results = [0,0,0]
  for ans_idx, ans in enumerate(answers):
    for man_idx, omr in enumerate(omrs):
      if omr[ans_idx % len(omr)] == ans:
        man_results[man_idx] += 1
  max_result = max(man_results)
  for idx, result in enumerate(man_results):
    if max_result == result:
      answer.append(idx+1)

  return answer


test_case = [
  [1, 3, 2, 4, 2], [1, 2, 3]
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
