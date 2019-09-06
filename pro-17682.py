def solution2(dartResult):
  answer = 0
  points= []
  idx = 0
  while idx < len(dartResult):
    # 숫자랑 제곱 읽기
    next_idx = 2
    if dartResult[idx+1].isdigit(): # 숫자가 2글자 인지 확인
      point = int(dartResult[idx] + dartResult[idx+1] )
      idx += 1
    else:
      point = int(dartResult[idx])
    multi = dartResult[idx+1]
    if multi == "S":
      multi = 1
    elif multi == "D":
      multi = 2
    else:
      multi = 3

    point_with_multi = point ** multi

    option = None

    if idx + 2 < len(dartResult):
      if not dartResult[idx+2].isdigit():
        option = dartResult[idx+2]
        next_idx += 1


    if option == "*":
      if len(points) > 0:
        points[-1] *= 2
      points.append(2*point_with_multi)
    elif option == "#":
      points.append(-point_with_multi)
    else:
      points.append(point_with_multi)

    # print(points)

    idx += next_idx
  for point in points:
    answer += point

  return answer


import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

test_case = [
  "1D2S#10S",  9
]

res = solution(test_case[0])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")