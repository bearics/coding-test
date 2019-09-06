def solution(n, arr1, arr2):
  answer = []
  base_maps_arrs = [arr1, arr2]
  base_maps = [[], []]
  for map_idx in range(2):  # 맵 종류
    for row in range(n):
      binary = "{0:b}".format(base_maps_arrs[map_idx][row])
      for i in range(n - len(binary[:])):
        binary = '0' + binary
      base_maps[map_idx].append(binary)
    print(base_maps[map_idx])

  for r in range(n):
    row_ans = ""

    for c in range(n):
      if base_maps[0][r][c] == base_maps[1][r][c] and base_maps[0][r][c] == "0":
        row_ans += " "
      else:
        row_ans += "#"
    answer.append(row_ans)

  return answer


test_case = [
  5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28], ["#####", "# # #", "### #", "#  ##", "#####"]
]

res = solution(test_case[0], test_case[1], test_case[2])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
