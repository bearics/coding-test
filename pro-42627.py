import heapq


def solution(jobs):
  answer = 0
  queue_list = []
  jobs = sorted(jobs)
  jobs_len = len(jobs)

  wait_time, now_time = 0, 0
  while True:
    if len(queue_list) == 0:
      first_job = jobs.pop(0)
      heapq.heappush(queue_list, (first_job[1], first_job[0]))  # length, start_time
    else:
      processing_length, processing_start_time = heapq.heappop(queue_list)
      if now_time < processing_start_time:
        wait_time += processing_length
        now_time += processing_length + (processing_start_time - now_time)
      else:
        wait_time += now_time - processing_start_time + processing_length
        now_time += processing_length
      for job in jobs[:]:
        if job[0] <= now_time:
          selected_job = jobs.pop(0)
          heapq.heappush(queue_list, (selected_job[1], selected_job[0]))
    if len(jobs) == 0 and len(queue_list) == 0:
      break
    # print(jobs, queue_list)
  answer = int(wait_time / jobs_len)
  return answer


test_case = [
  [[0, 3], [1, 9], [2, 6], [20, 5]], 9
  #   [[0, 5], [1, 2], [5, 5]], 6
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
