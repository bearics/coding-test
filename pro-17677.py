def solution(str1, str2):
  answer = 0
  str_sets = [[], []]
  input_strings = [str1.lower(), str2.lower()]

  for str_idx in range(2):
    string = input_strings[str_idx]
    length = len(string)
    for idx in range(length):
      if idx + 1 < length:
        if string[idx].isalpha() and string[idx + 1].isalpha():
          str_sets[str_idx].append(string[idx] + string[idx + 1])
    print(str_sets[str_idx])

  a_s, b_s = str_sets[0][:], str_sets[1][:]
  intersection_set = []
  for a in a_s:
    if a in b_s:
      b_s.remove(a)
      intersection_set.append(a)
  union_set = a_s + b_s
  try:
    answer = int((len(intersection_set) / len(union_set)) * 65536)
  except ZeroDivisionError:
    answer = 65536

  return answer


test_case = [
  "aa1+aa2", "AAAA12", 43690
]

res = solution(test_case[0], test_case[1])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
