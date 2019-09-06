def solution(routes):
  answer = 0
  routes = sorted(routes)
  candidate_timeline_list = []
  for route in routes:
    candidate_timeline_list.append(route[0])
    candidate_timeline_list.append(route[1])
  candidate_timeline_list = sorted(list(set(candidate_timeline_list)))
  # print(candidate_timeline_list)

  start_idx, last_idx = 0, 0
  min_right = candidate_timeline_list[-1]
  for candidate_timeline in candidate_timeline_list:
    # 시작부터 끝 까지 만족하는가?
    # print(start_idx, last_idx, min_right, candidate_timeline)
    if min_right < candidate_timeline:
      # print("he")
      answer += 1
      min_right = candidate_timeline_list[-1]
      start_idx = last_idx + 1


    if start_idx <= last_idx and  candidate_timeline_list[-1] == candidate_timeline == min_right:
      answer += 1
      break

    for route_idx in range(start_idx, len(routes)):
      if routes[route_idx][0] <= candidate_timeline <= routes[route_idx][1]:
        min_right = min(min_right, routes[route_idx][1])
        last_idx = route_idx
      else:
        break
  return answer


test_case = [
  # [[-20, 15], [-14, -5], [-18, -13], [-5, -3]], 2
  [[0, 1], [0, 1], [0, 1]], 1
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
