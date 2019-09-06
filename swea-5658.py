import heapq

case_num = int(input())

for case_idx in range(1, case_num+1):
  N, K = map(int, input().split())
  input_number = str(input())
  side_len =int( N / 4 )
  side_numbers_heap = []
  for idx in range(side_len):
    temp_number = input_number[idx:]
    for j in range(idx):
      temp_number += input_number[j]
    for j in range(4):
      num = int(temp_number[side_len*j:side_len*(j+1)], 16)
      if not num in side_numbers_heap:
        heapq.heappush(side_numbers_heap, num)
      # side_numbers_heap.append(int(temp_number[side_len*j:side_len*(j+1)], 16))
  result_len = len(side_numbers_heap)
  for _ in range(result_len-K):
    heapq.heappop(side_numbers_heap)
  print("#{} {}".format(case_idx, heapq.heappop(side_numbers_heap)))
