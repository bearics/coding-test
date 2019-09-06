from functools import cmp_to_key

def cmp_str(p1, p2):
  p1, p2 = str(p1), str(p2)
  if int(p1 + p2) > int(p2 + p1):
    return 1
  else:
    return -1


def solution(numbers):
  answer = ''
  dic = {}
  keys = []
  for number in numbers:
    first_num = number
    while True:
      if first_num < 10:
        break
      first_num = int(first_num / 10)
    if not first_num in dic:
      dic[first_num] = []
    dic[first_num].append(number)

  for key in dic:
    dic[key] = sorted(dic[key], key=cmp_to_key(cmp_str), reverse=True)
    keys.append(key)
  keys = sorted(keys, reverse=True)

  for k in keys:
    number_list = dic[k]
    for num in number_list:
      answer += str(num)
  # print(dic)
  answer = str(int(answer))

  return answer

test_case = [
  # [6, 10, 2], "6210"
	[3, 30, 34, 5, 9], "9534330"
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")