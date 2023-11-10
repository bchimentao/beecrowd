# 2163 - O Despertar da Força

N, M = map(int, input().split(' '))

linhas = []
for i in range(N):
  linhas.append(input().split(' '))

x = 0
y = 0

for n in range(N):
  if n == 0 or n == (N - 1):
    continue
  for m in range(M):
    if m == 0 or m == (M - 1):
      continue
    if linhas[n][m] == '42':
      if linhas[n-1][m-1] == '7' \
      and linhas[n-1][m] == '7' \
      and linhas[n-1][m+1] == '7' \
      and linhas[n][m+1] == '7' \
      and linhas[n][m+1] == '7' \
      and linhas[n+1][m-1] == '7' \
      and linhas[n+1][m] == '7' \
      and linhas[n+1][m+1] == '7':
        x = n + 1
        y = m + 1

print(x, y)