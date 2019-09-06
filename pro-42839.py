from itertools import permutations

def solution(numbers):
  answer = 0
  nums = []
  for c in range(len(numbers)):
    nums.append(numbers[c])
  # print(nums)

  candidate_list = []
  for n in range(1, len(nums) + 1):
    temp_list = (list(map(''.join, permutations(nums, n))))
    temp_list = list(map(int, temp_list))
    candidate_list= list(set(candidate_list + temp_list))
    # print(candidate_list)

  for candidate in candidate_list:
    is_prime = True
    for i in range(2, candidate):
      if candidate % i == 0:
        is_prime = False
        break
    if is_prime == True and candidate != 1 and candidate != 0:
      # print(candidate)
      answer += 1


  return answer

test_case = [
  "17", 3
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
