def solution(operations):
  answer = []
  numbers = []
  for operation in operations:
    op = operation.split(' ')
    if op[0] == "I":
      op_num = int(op[1])
      if len(numbers) == 0:
        numbers.append(op_num)
      else:
        idx = 0
        while idx < len(numbers):
          if op_num <= numbers[idx]:
            break
          idx += 1
        numbers.insert(idx, op_num)

    elif op[0] == "D":
      if op[1] == "1":  # 최댓값 삭제
        if numbers:
          numbers.pop(-1)
      elif op[1] == "-1":  # 최솟값 삭제
        if numbers:
          numbers.pop(0)

  if numbers:
    answer.append(numbers[-1])
    answer.append(numbers[0])
  else:
    answer.append(0)
    answer.append(0)

  return answer


test_case = [
  # ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"], [0, 0]
  ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"], [333, -45]
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
