def time_to_int(str_time):
  return (int(str_time.split(":")[0]) * 60) + int(str_time.split(":")[1])


def solution(n, t, m, timetable):
  answer = ''
  start_time = 540
  timetable = sorted(list(map(time_to_int, timetable)))
  on_bus_lists = [[] for _ in range(n)]

  for shuttle in range(n):
    for man in range(m):  # 최대 m명까지 탈 수 있음
      if len(timetable) > 0:
        if timetable[0] <= start_time + (shuttle * t):
          on_bus_lists[shuttle].append(timetable.pop(0))
      else:  # 더이상 탈 사람이 안옴
        break

  on_bus_list = on_bus_lists[-1]
  if len(on_bus_list) >= m:
    answer = list(set(on_bus_list))[-1] - 1
  else:
    answer = start_time + (t * (n - 1))

  print(on_bus_lists)
  return "{:02d}:{:02d}".format(answer // 60, answer % 60)


test_case = [
  2, 10, 2, ["09:10", "09:09", "08:00"], "09:09"
]

res = solution(test_case[0], test_case[1], test_case[2], test_case[3])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
