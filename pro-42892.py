import sys

sys.setrecursionlimit(10 ** 6)

y_list_dic = {}
max_height = 0
pre_t, post_t = [], []


class Node:
  def __init__(self, val, x, left=None, right=None):
    self.val = val
    self.x = x
    self.left = left
    self.right = right


def set_subtree(now_node, height, left_limit, right_limit):
  if height >= max_height:
    return

  nodes = y_list_dic[list(y_list_dic.keys())[height]]  # 다음층 노드들(정렬되어 있음)
  for idx, (x, val) in enumerate(nodes[:]):
    if x > right_limit:
      break

    if left_limit < x and x < now_node.x:  # left subtree
      nodes.pop(0)
      now_node.left = Node(val, x)
      set_subtree(now_node.left, height + 1, left_limit, now_node.x)
    elif now_node.x < x and x < right_limit:  # right subtree
      nodes.pop(0)
      now_node.right = Node(val, x)
      set_subtree(now_node.right, height + 1, now_node.x, right_limit)


def preorder_trav(node):
  global pre_t
  if node != None:
    pre_t.append(node.val)
    preorder_trav(node.left)
    preorder_trav(node.right)


def postorder_trav(node):
  global post_t
  if node != None:
    postorder_trav(node.left)
    postorder_trav(node.right)
    post_t.append(node.val)


def solution1(nodeinfo):
  answer = []

  global max_height
  global y_list_dic

  for idx, node in enumerate(nodeinfo):
    if not node[1] in y_list_dic:
      y_list_dic[node[1]] = []
    y_list_dic[node[1]].append((node[0], idx + 1))
  y_list_dic = dict(sorted(y_list_dic.items(), reverse=True))
  for y_key in y_list_dic:
    y_list_dic[y_key] = sorted(y_list_dic[y_key], key=lambda i: i[0])
  max_height = len(y_list_dic)
  x, val = y_list_dic[list(y_list_dic.keys())[0]][0]
  root = Node(val, x)
  set_subtree(root, 1, -1, 10000000)
  print("wa")
  preorder_trav(root)
  postorder_trav(root)
  answer.append(pre_t)
  answer.append(post_t)

  return answer

#############################################################################################################

preorder = list() # 귀찮아서 전역으로
postorder = list()
def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**6)
    levels = sorted(list({x[1] for x in nodeinfo}),reverse=True) # 유효한 Y좌표
    print(list(zip(range(1,len(nodeinfo)+1),nodeinfo)))
    nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬
    order(nodes,levels,0)
    return [preorder,postorder]

def order(nodes,levels,curlevel):
    n = nodes[:] # copy
    cur = n.pop(0) # VISIT
    preorder.append(cur[0]) # PRE-ORDER
    if n: # stop if leaf node
        for i in range(len(n)): # find next floor
            if n[i][1][1] == levels[curlevel+1]: # next floor
                if n[i][1][0] < cur[1][0]: # LEFT CHILD
                    order([x for x in n if x[1][0] < cur[1][0]],levels,curlevel+1)
                else: # RIGHT CHILD
                    order([x for x in n if x[1][0] > cur[1][0]],levels,curlevel+1)
                    break
    postorder.append(cur[0]) # POST-ORDER

test_case = [
  [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]],  # test_case
  [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]  # result
]

res = solution(test_case[0])
print(res)
if res == test_case[-1]:
  print("goood")
else:
  print("fail ")
