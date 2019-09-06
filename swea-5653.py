dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # left, top, right, bottom (x,y)

class Cell:
  def __init__(self, y, x, num):
    self.y = y
    self.x = x
    self.num = num
    self.life = num

  def change(self):
    self.life = self.num

  def go(self):  # 시간이 지남
    if self.life <= 1:
      self.change()
      return True  # 활성화 됨.
    else:
      self.life -= 1
      return False  # 아직 변화 없음


CENTER = 500
case_num = int(input())
for case_idx in range(1, case_num + 1):
  N, M, K = list(map(int, input().split()))
  base_map = [[0] * (CENTER * 2) for _ in range(CENTER * 2)]
  active_cells = []
  inactive_cells = []

  for r in range(N):
    # for c, cell in enumerate(list(map(lambda i: CellPair(i, 0), input().split()))):
    for c, cell in enumerate(list(map(int, input().split()))):
      base_map[CENTER + r][CENTER + c] = cell
      if cell > 0:
        inactive_cells.append(Cell(CENTER + r, CENTER + c, cell))
  # print(base_map)

  # init

  for t in range(1, K+1):
    delete_list = []
    new_active_cells = []
    for idx, inactive_cell in enumerate(inactive_cells):
      y, x = inactive_cell.y, inactive_cell.x
      is_changed = inactive_cell.go()
      if is_changed:  # 활성화 됨
        delete_list.append(idx)
        new_active_cells.append(Cell(inactive_cell.y, inactive_cell.x, inactive_cell.num))
    for idx in reversed(delete_list):
      inactive_cells.pop(idx)
    # print(deative_cells)

    delete_list = []
    active_cells = sorted(active_cells, key=lambda i: i.num, reverse=True)
    for idx, active_cell in enumerate(active_cells):
      # 번식을 한다
      y, x, num = active_cell.y, active_cell.x, active_cell.num
      for dx, dy in dirs:
        prev_num = base_map[y + dy][x + dx]
        if prev_num == 0:  # 자리가 비어 있을 때
          base_map[y + dy][x + dx] = num
          inactive_cells.append(Cell(y + dy, x + dx, num))

      is_changed = active_cell.go()
      if is_changed:  # 세포 죽음
        base_map[y][x] = 100
        delete_list.append(idx)
    for idx in reversed(delete_list):
      active_cells.pop(idx)

    for new_active_cell in new_active_cells:
      active_cells.append(Cell(new_active_cell.y, new_active_cell.x, new_active_cell.num))
    # print("dd")
  print("#{} {}".format(case_idx, len(active_cells) + len(inactive_cells)))
