def solution(name):
  answer = 0
  need_to_change_idx_list = []
  for i, c in enumerate(name):
    if c != 'A':
      num_char = ord(c)
      if num_char <= 78:
        answer += num_char - 65
      else:
        answer += 90 - num_char + 1
      if i != 0:
        need_to_change_idx_list.append(i)
  # print(answer)
  # print(need_to_change_idx_list[:-1])
  answers = []
  if len(need_to_change_idx_list) >= 2:
    answers.append(need_to_change_idx_list[-1])
    answers.append(len(name) - need_to_change_idx_list[0])
    for i, turn_idx in enumerate(need_to_change_idx_list[:-1]):
      print(turn_idx, 2*turn_idx + len(name) - need_to_change_idx_list[i+1])
      answers.append(2*turn_idx + len(name) - need_to_change_idx_list[i+1])
  elif len(need_to_change_idx_list) == 1:
    answers.append(need_to_change_idx_list[0])
    answers.append(len(name) - need_to_change_idx_list[0])
  else:
    pass
  # print(answers)
  try:
    answer += min(answers)
  except ValueError:
    answer += 0




  return answer


test_case = [
  # "BAB", 3
  # "CACAAAAAAAAAAAAAAAAAAAAAAAAAC", 11
  # "CACAAAACAC", 15
"AAAZAAZA", 7
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
