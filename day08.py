###           v----------(update these)---v
with open("day08.txt",'r') as aoc_input: map = aoc_input.readlines()

map = [R.copy() for R in map]
H,W=len(map),len(map[-1])
antinodes = [[0]*len(map[-1]) for R in map]
antlocs = dict()
for i in range(W):
  for j in range(H):
    l=map[i][j]
    if not '.'==l:
      antlocs[l].append((i,j)) if l in antlocs.keys() else antlocs[l] = [(i,j)]
print(antlocs)
