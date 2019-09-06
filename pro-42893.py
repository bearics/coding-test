import re


class WebPage:
  def __init__(self, index):
    self.url = ""
    self.links = []
    self.base_point = 0
    self.link_point = 0
    self.matching_point = 0
    self.index = index

  def __repr__(self):
    return "[{}] mp: {}, url : {} links : {}\n".format(self.index, self.matching_point, self.url, self.links)


def solution(word, pages):
  answer = 0
  web_pages = []
  link_points = {}
  for idx, page in enumerate(pages):
    web_page = WebPage(idx)
    web_pages.append(web_page)
    web_page.url = re.search(r"<meta property=\"og:url\" content=\"https://(.*)\"/>", page).group(1)
    web_page.links = list(re.findall(r"<a href=\"https://(.*)\">", page))

    p = re.compile(word, re.I)
    res_words = p.finditer(page)
    for res_word in res_words:
      start, end = res_word.span()
      if start - 1 < 0 or end >= len(page):
        continue

      if (not page[start-1].isalpha()) and (not page[end].isalpha()):
        web_page.base_point += 1

    for link in web_page.links:
      if link in link_points:
        link_points[link] = link_points[link] + (web_page.base_point / len(web_page.links))
      else:
        link_points[link] = web_page.base_point / len(web_page.links)

  for web_page in web_pages:
    if web_page.url in link_points:
      web_page.link_point = link_points[web_page.url]
    web_page.matching_point = web_page.base_point + web_page.link_point

  web_pages = sorted(web_pages, key=lambda i: (i.matching_point, -i.index), reverse=True)
  print(web_pages)

  return web_pages[0].index

def getScore(word, page):
  import re
  return re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())


def solution2(word, pages):
  webpages = {}
  for i, page in enumerate(pages):
    pagetitle = page.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
    links = []
    for link_long in page.split('a href=\"')[1:]:
      links.append(link_long.split('\"')[0])
    webpages[pagetitle] = [i, getScore(word, page), links, 0]  # 3은 링크점수

  for page in webpages.values():
    for target in page[2]:
      try:
        webpages[target][3] += page[1] / len(page[2])
      except:
        pass
  answer = []
  print(webpages)
  for page in webpages.values():
    answer.append([page[0], page[1] + page[3]])

  answer.sort(key=lambda x: x[0])
  return sorted(answer, key=lambda x: x[1], reverse=True)[0][0]


# test_case = [
#   "blind",
#   ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"],
#   0# result
# ]

test_case = [
  "blind", [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"],
  0  # result
]

res = solution(test_case[0], test_case[1])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
