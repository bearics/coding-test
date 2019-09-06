from collections import OrderedDict

def solution1(food_times, k):
  answer = -1
  ranked_food = set(sorted(food_times))
  count_food = len(food_times)
  print(ranked_food)
  prev_food = 0
  for r in ranked_food:
    lowest_time = r - prev_food
    prev_food = r
    if k < lowest_time * count_food:
      count = (k % count_food) + 1
      answer = 0
      while count > 0:
        if food_times[answer] > 0:
          count -= 1
        answer += 1
      break
    else:
      count_zero = 0
      for idx in range(len(food_times)):
        food_times[idx] -= lowest_time
        if food_times[idx] == 0:
          count_zero += 1
      k -= lowest_time * count_food
      count_food -= count_zero

  return answer

def solution2(food_times, k):
  answer = -1
  ranked_foods = {} # {value : [idx...] ... }
  count_all_food = len(food_times)

  for idx, food_time in enumerate(food_times):
    if not food_time in ranked_foods:
      ranked_foods[food_time] = ([])
    ranked_foods[food_time].append(idx)
  ranked_foods = dict(sorted(ranked_foods.items()))
  count_zero_food_time = 0
  prev_lowest_time = 0
  for key in ranked_foods:
    lowest_time_foods = ranked_foods[key]
    lowest_time = food_times[lowest_time_foods[0]] - prev_lowest_time
    prev_lowest_time = food_times[lowest_time_foods[0]]
    if k < lowest_time * (count_all_food - count_zero_food_time):
      count = (k % (count_all_food - count_zero_food_time)) + 1
      answer = 0
      while count > 0:
        if food_times[answer] > 0:
          count -= 1
        answer += 1
      break
    else:
      k -= lowest_time * (count_all_food - count_zero_food_time)
      for lowest_time_food in lowest_time_foods:
        food_times[lowest_time_food] = 0
        count_zero_food_time += 1


  return answer

def solution(food_times, k):
  food_times_dic = {}
  food_times_list = []
  totalTime = 0

  for i in range(0, len(food_times)):
    food_times_list.append([i, food_times[i]])
    totalTime += food_times[i]

  if totalTime <= k:
    return -1

  food_times_list = sorted(food_times_list, key=lambda x: x[1])

  delTime = food_times_list[0][1] * len(food_times_list)
  i = 1
  # print k
  # print delTime
  while delTime < k:
    k -= delTime
    delTime = (food_times_list[i][1] - food_times_list[i - 1][1]) * (len(food_times_list) - i)
    # print k, delTime
    i += 1

  food_times_list = sorted(food_times_list[i - 1:], key=lambda x: x[0])
  # print food_times_list
  # print k
  return food_times_list[k % len(food_times_list)][0] + 1

food_times1 = [5,2,2]
k1 = 7
result1 = 1

if solution(food_times1, k1) == result1:
  print("goood")
else:
  print("fail ")
