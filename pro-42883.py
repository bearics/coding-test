def solution(number, k):
  stack = [number[0]]
  for num in number[1:]:
    while len(stack) > 0 and stack[-1] < num and k > 0:
      k -= 1
      stack.pop()
    stack.append(num)
  if k != 0:
    stack = stack[:-k]
  return ''.join(stack)


test_case = [
  # "2311111111", 3, "3111111"
  # "2311", 1, "311"
  # "23111", 2, "311"
  # "4177252841", 4, "775841"
  "1010", 2, "11"
  # "1231234", 3, "3234"
  #                    "21111", 4, "2"
]

res = solution(test_case[0], test_case[1])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
