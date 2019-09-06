import collections

def solution(cacheSize, cities):
  answer = 0
  cache_deque = collections.deque()

  cities = list(map(lambda i: i.lower(), cities))

  for city in cities:
    if city in cache_deque:
      answer += 1
    else:
      answer += 5

    if cacheSize > 0:
      if len(cache_deque) >= cacheSize: # 캐시 꽉참
        if city in cache_deque:
          cache_deque.remove(city)
        else:
          cache_deque.popleft()
        cache_deque.append(city)
      else:
        cache_deque.append(city)


  return answer

test_case = [
  # 3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"], 50
	# 3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"], 21
	5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], 52
]

res = solution(test_case[0], test_case[1])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
