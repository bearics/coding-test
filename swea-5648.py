import heapq

CENTER = 1000
dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]  # (y, x)
case_num = int(input())

for case_idx in range(1, case_num + 1):
  atom_num = int(input())
  atoms = []  # [x, y, d, k]
  for _ in range(atom_num):
    atoms.append(list(map(int, input().split())))

  # base_map = [[-1 for _ in range(2001)] for _ in range(2001)]
  for idx, atom in enumerate(atoms):
    atom[0], atom[1] = float(atom[0] + CENTER), float(atom[1] + CENTER)
    # base_map[0][atom[1]][atom[0]] = idx

  all_energy = 0
  tick = 0.5
  for _ in range(4002):
    move_dict = {}
    delete_atoms = []

    for idx, atom in enumerate(atoms):
      dy, dx = dirs[atom[2]]
      atom[0], atom[1] = atom[0] + (tick * dx), atom[1] + (tick * dy)
      if atom[0] < 0 or atom[0] > 2000 or atom[1] < 0 or atom[1] > 2000:
        delete_atoms.append(idx)
        continue
      if not (atom[0], atom[1]) in move_dict:  # (x, y)
        move_dict[(atom[0], atom[1])] = []
      move_dict[(atom[0], atom[1])].append(idx)

    for key in move_dict:
      move = move_dict[key]
      if len(move) >= 2:
        for atom_idx in move:
          delete_atoms.append(atom_idx)
          all_energy += atoms[atom_idx][3]

    for delete_atom in reversed(delete_atoms):
      atoms.pop(delete_atom)

    if len(atoms) < 2:
      break

  # result
  print("#{} {}".format(case_idx, all_energy))
