def solution(people, limit):
  answer = len(people)
  people = sorted(people)

  count = 0
  start_idx, end_idx = 0, len(people) -1
  while start_idx < end_idx:
    if people[start_idx] + people[end_idx] <= limit:  # 같이 탐
      count += 1
      start_idx += 1
      end_idx -= 1
    else: # 무거운 사람 혼자 타야해
      end_idx -= 1
    # min_weight = people[start_idx]
    #
    #
    # while len(people) > 0 and min_weight + people[-1] > limit:
    #   people.pop()
    #
    # if len(people) > 0:
    #   count += 1
    #   people.pop()
  answer -= count
  return answer


test_case = [
  # [70, 80, 50], 100, 3
  # [50], 100, 3
  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 100, 6
]

res = solution(test_case[0], test_case[1])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
