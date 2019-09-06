def solution(msg):
  answer = []
  dic = {}
  dic_num = 26
  for i in range(1,27):
    dic[chr(i+64)] = i

  idx = 0
  while idx < len(msg):
    sb = ''
    is_in_dic = None
    for j in range(len(msg) - idx):
      is_in_dic = None
      sb += msg[idx + j]
      if sb in dic:
        is_in_dic = True
        continue
      else:
        dic_num += 1
        dic[sb] = dic_num
        is_in_dic = False
        break;
    if is_in_dic == True:
      answer.append(dic[sb])
      idx += len(sb)
    else:
      answer.append(dic[sb[:-1]])
      idx += len(sb[:-1])



  return answer


test_case = [
  "KAKAO", [11, 1, 27, 15]
	# "TOBEORNOTTOBEORTOBEORNOT", [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
]

res = solution(test_case[0])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
