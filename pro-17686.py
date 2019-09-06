import re


def solution(files):
  answer = []
  sorted_files = []  # [ [idx, default_file, (head, num, idx) ]]
  p = re.compile(r"([^0-9]+)([0-9]{1,5})")

  for idx, file in enumerate(files):
    head, num = p.findall(file.lower())[0]
    # print(idx, head, num)
    sorted_files.append([idx, file, (head, int(num), idx)])

  sorted_files = sorted(sorted_files, key=lambda i: i[2])
  for sorted_file in sorted_files:
    answer.append(sorted_file[1])
  print(sorted_files)

  return answer


test_case = [
  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
  ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
]

res = solution(test_case[0])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
