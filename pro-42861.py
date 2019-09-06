parent = {}
rank = {}

# 정점을 독립적인 집합으로 만든다.
def make_set(v):
  parent[v] = v
  rank[v] = 0


# 해당 정점의 최상위 정점을 찾는다.
def find(v):
  if parent[v] != v:
    parent[v] = find(parent[v])

  return parent[v]

# 두 정점을 연결한다.
def union(v, u):
  root1 = find(v)
  root2 = find(u)

  if root1 != root2:
    # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
    if rank[root1] > rank[root2]:
      parent[root2] = root1
    else:
      parent[root1] = root2

      if rank[root1] == rank[root2]:
        rank[root2] += 1

def kruskal(graph):
  for v in graph['vertices']:
    make_set(v)

  mst = []

  edges = graph['edges']
  edges.sort()

  for edge in edges:
    weight, v, u = edge

    if find(v) != find(u):
      union(v, u)
      mst.append(edge)

  return mst


def solution(n, costs):
  # answer = 0
  # cost_dic = {}
  # for cost in costs:
  #   if not cost[2] in cost_dic:
  #     cost_dic[cost[2]] = []
  #   cost_dic[cost[2]].append([cost[0], cost[1]])
  # cost_keys = sorted(list(set([cost[2] for cost in costs])))
  # # print(cost_dic, cost_keys)
  #
  # check_list = [False for _ in range(n)]
  # fin_check_list = [False] + [True for _ in range(n-1)]
  #
  # for cost_key in cost_keys:
  #   cost_list = cost_dic[cost_key]
  #   for cost in cost_list:
  #     if cost[0] < cost[1]:
  #       r, c = cost[0], cost[1]
  #     else:
  #       r, c = cost[1], cost[0]
  #     if check_list[c] == False:
  #       # print(r, c)
  #       answer += cost_key
  #       check_list[c] = True
  #     if check_list == fin_check_list:
  #       break



  #
  # for cost_level in cost_rank:
  #   for cost in costs:
  #     if cost[2] == cost_level:

  # print(costs, cost_rank)

  # for cost in costs:
  #   cost_map[cost[0]][cost[1]] = cost[2]
  #   cost_map[cost[1]][cost[0]] = cost[2]
  #
  # check_list = [ i for i in range(n)]
  # for r in range(n-1):
  #   min_cost = 9999999999
  #   save_pos = (-1, -1) # (r,c)
  #   for c in range(n):
  #     if cost_map[r][c] != 0 and cost_map[r][c] < min_cost and c in check_list:
  #       min_cost = cost_map[r][c]
  #       save_pos = (r, c)
  #   answer += min_cost
  #   check_list.remove(save_pos[1])
  #   cost_map[save_pos[0]][save_pos[1]] = 0
  #   cost_map[save_pos[1]][save_pos[0]] = 0

  # for row in cost_map:
  #   print(*row)

  answer = 0
  graph = {
    'vertices': [],
    'edges': [
    ]
  }
  for n in range(n):
    graph['vertices'].append(str(n))

  for cost in costs:
    graph['edges'].append((cost[2], str(cost[0]), str(cost[1])))
    graph['edges'].append((cost[2], str(cost[1]), str(cost[0])))

  msts = kruskal(graph)
  for mst in msts:
    answer += mst[0]
  return answer


test_case = [
  4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]], 4
  # 4, [[0, 2, 1], [1, 2, 2], [1, 3, 3]], 6

]

res = solution(test_case[0], test_case[1])
print("------result------")
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
