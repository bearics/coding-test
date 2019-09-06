from itertools import permutations


# def solve(candidate, depth):
#   if depth >= max_depth:
#     is_ok = True
#     for i in range(3):
#       if len(candidate[i]) == 0:
#         is_ok = False
#         break
#
#     if is_ok == True:
#       print(candidate)
#     #
#     # global answers
#     # answers.append()
#
#   numbers, strike, ball = baseballs[depth]
#   sb = []
#   for s in range(strike):
#     sb.append('s')
#   for b in range(ball):
#     sb.append('b')
#   for o in range(3 - strike - ball):
#     sb.append('o')
#   set_list = list(set(list(map(''.join, permutations(sb, 3)))))
#   print(set_list)
#   for s in set_list:
#
#     is_ok = True
#     for i in range(len(s)):
#       if s[i] == 's':
#         strike_num = int(str(numbers)[i])
#         if not strike_num in candidate[i]:
#           is_ok = False
#           print("die, s",i,strike_num)
#           break
#         else:
#           candidate[i] = [int(str(numbers)[i])]
#       elif s[i] == 'b': # 다른 곳에 b가 있는지 확인 없으면 끝
#         ball_num = int(str(numbers)[i])
#         rest_candidate = []
#         rest_i = [0, 1, 2]
#         rest_i.remove(i)
#         for j in rest_i:
#           rest_candidate.extend(candidate[j])
#         if ball_num in candidate[i]:
#           candidate[i].remove(ball_num)
#         if not ball_num in rest_candidate:
#           is_ok = False
#           print("die, b",i,ball_num)
#           break
#       elif s[i] == 'o':
#         out_number = int(str(numbers)[i])
#         for j in range(3):
#           if out_number in candidate[i]:
#             candidate[i].remove(out_number)
#
#     print(depth, s, candidate)
#     for i in range(3):
#       if len(candidate[i]) == 0:
#         is_ok = False
#         print("die, {} is empty".format(i))
#         break
#
#     if is_ok == True:
#       solve(candidate[:], depth + 1)


def solution(baseball):
  answer = 0
  candidate = [[i for i in range(1, 10)] for _ in range(3)]
  for i in range(1,10):
    for j in range(1, 10):
      if j == i:
        continue
      for k in range(1, 10):
        if k == i or k == j:
          continue
        is_suc = True
        for line in baseball:
          nums, strike, ball = line
          test_strike, test_ball = 0, 0
          test_nums = [i, j, k]
          nums = [int(c) for c in str(nums)]
          for idx in range(3):
            if test_nums[idx] == nums[idx]:
              test_strike += 1
            else:
              if test_nums[idx] in nums:
                test_ball += 1
          if not (test_strike == strike and test_ball == ball):
            is_suc = False
            break
        if is_suc == True:
          answer += 1
  return answer


test_case = [
  [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]], 2
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
