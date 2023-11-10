# 1098 - Sequencia IJ 4

for i in range(0, 21, 2):
  if i in [0, 10, 20]:
    i = int(i/10)
  else:
    i = i/10
  for j in range(1, 4):
    print(f'I={i} J={j+i}')