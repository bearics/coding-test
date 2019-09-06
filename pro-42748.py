def solution(array, commands):
  answer = []
  for com in commands:
    start, end, selected_idx = com
    selected_array = array[start-1:end]
    sorted_array = sorted(selected_array)
    answer.append(sorted_array[selected_idx-1])
  return answer


test_case = [
  [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]], [5, 6, 3]
]

res = solution(test_case[0], test_case[1])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
