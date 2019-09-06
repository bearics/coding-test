
def solution(n, lost, reserve):
  answer = 0
  students = [i+1 for i in range(n)]
  for lost_student in lost[:]:
    if lost_student in reserve:
      reserve.remove(lost_student)
      lost.remove(lost_student)

  for l in lost[:]:
    is_ok = False
    if l-1 in reserve:
      reserve.remove(l-1)
      is_ok = True
    elif l+1 in reserve:
      reserve.remove(l + 1)
      is_ok = True
    if is_ok == True:
      lost.remove(l)

  answer = n - len(lost)




  return answer


test_case = [
  5, [2, 4], [3],  4
]

res = solution(test_case[0], test_case[1], test_case[2])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
