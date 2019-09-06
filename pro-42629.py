import heapq


def solution(stock, dates, supplies, k):
  answer = 0
  supply_dates = []
  for i, (d, s) in enumerate(zip(dates, supplies)):
    supply_dates.append((-s, d, s))  # (supply, dates)
  # print(supply_dates)
  day = 0
  supply_date_idx_list = [idx for idx in range(len(supply_dates))]
  can_supply = []
  while day + stock < k:
    for idx in supply_date_idx_list[:]:
      supply_date_set = supply_dates[idx]
      if supply_date_set[1] <= day + stock:
        heapq.heappush(can_supply, supply_date_set)
        supply_date_idx_list.remove(idx)
      else:
        break
    # print(can_supply)
    if len(can_supply) > 0:
      _, selected_date, selected_supply = heapq.heappop(can_supply)
      # print(selected_date, selected_supply)
      if selected_date > day:
        stock = stock - (selected_date - day) + selected_supply
        day = selected_date
      else:
        stock = stock + selected_supply
      # print(day, stock, selected_date, selected_supply)
      answer += 1


  return answer


test_case = [
  # 4, [1, 4, 5, 6, 7, 8], [1, 2, 1, 3, 2, 1], 11, 3
  4, [4,5,6], [2,1,2], 9,3
  # 1, [1, 2, 3, 4, 5], [1, 1, 1, 1, 1], 6, 5
  # 1, [1, 2, 3, 4, 5], [1, 1, 1, 1, 1], 1, 0

  # 4, [4, 10, 15], [20, 5, 10], 30, 2
]

res = solution(test_case[0], test_case[1], test_case[2], test_case[3])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
