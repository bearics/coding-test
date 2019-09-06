def sol():
  return 0


N = int(input())
tri = []
dp = [[0]*N for _ in range(N)]
for row in range(N):
  tri.append(list(map(int, input().split())))

for r in range(len(tri)):
  for c in range(len(tri[r])):
    if r == 0 and c == 0:
      dp[r][c] = tri[r][c]
    elif (c == 0 and r != 0):
      dp[r][c] = tri[r][c] + dp[r - 1][c]
    elif (c == r and r != 0):
      dp[r][c] = tri[r][c] + dp[r - 1][c - 1]
    else:
      dp[r][c] = tri[r][c] + max(dp[r - 1][c], dp[r - 1][c - 1])

max_ans = 0
for idx in range(N):
  max_ans = max(dp[N-1][idx], max_ans)

print(max_ans)