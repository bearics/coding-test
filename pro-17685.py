def solution(words):
  answer = 0
  dic = { 'count' : 0}

  for word in words:
    target_dic = dic
    for idx in range(0, len(word)):
      w = word[idx]
      if not w in target_dic:
        target_dic[w] = { 'count' : 1}
      else:
        target_dic[w]['count'] += 1
      target_dic = target_dic[w]
  # print(dic)

  for word in words:
    target_dic = dic
    for idx in range(0, len(word)):
      w = word[idx]
      if idx == len(word) - 1:
        answer += idx + 1
        break
      if target_dic[w]['count'] <= 1:
        answer += idx + 1
        break
      else:
        target_dic = target_dic[w]

  # for word in words:
  #   for idx in range(1, len(word) + 1):
  #     if word[:idx] in dic:
  #       dic[word[:idx]] += 1
  #     else:
  #       dic[word[:idx]] = 1
  #   print(dic)
  #
  # for word in words:
  #   for idx in range(1, len(word) + 1):
  #     if idx == len(word):
  #       answer += idx
  #       break
  #     if dic[word[:idx]] == 1:
  #       answer += idx
  #       break



  # print(dic)

    # for idx in range(1, len(word) + 1):
    #   print(1, end=" ")
    #   if idx == len(word):
    #     answer += len(word)
    #     break
    #   search_word = word[:idx]
    #   count_search_result = 0
    #   for sword in words:
    #     try:
    #       if search_word == sword[:idx]:
    #         count_search_result += 1
    #     except IndexError:
    #       continue
    #   if count_search_result == 1:  # 하나만 검색됨
    #     # print(search_word)
    #     answer += idx
    #     break


  return answer


test_case = [
  ["go", "gone", "guild"], 7
]

res = solution(test_case[0])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
