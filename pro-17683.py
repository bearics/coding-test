import re

def time_to_int(str_time):
  return int(str_time.split(":")[0]) * 60 + int(str_time.split(":")[1])


def solution(m, musicinfos):
  answer = ''
  mi = []
  p = re.compile("([A-Z][#]?)")
  m = p.findall(m)
  for musicinfo in musicinfos:
    options = musicinfo.split(",")
    options[0] = time_to_int(options[0])
    options[1] = time_to_int(options[1])
    options.append(options[1] - options[0])
    options[3] = p.findall(options[3])
    play_music = []
    for i in range(options[4]):
      play_music.append(options[3][i % len(options[3])])
    options.append(play_music)

    options.append(False)
    for i in range(options[4] - len(m) + 1):
      # print(m, options[5][i:i + len(m)])
      if m == options[5][i:i+len(m)]:
        options[-1] = True

    mi.append(options)

  # print(mi)

  rank = []
  for idx, music in enumerate(mi):
    if music[6] == True:
      rank.append((music[4], -idx))
  rank = sorted(rank, reverse=True)

  # print(rank)
  try:
    answer = mi[-rank[0][1]][2]
  except IndexError:
    answer = "`(None)`"
  return answer


test_case = [
  "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], "HELLO"
]

res = solution(test_case[0], test_case[1])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
