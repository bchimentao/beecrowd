# 2842 - Dabriel e Suas Strings

A = input()
B = input()

len_A = len(A)
len_B = len(B)

DP = [[0] * (len_B + 1) for _ in range(len_A + 1)]

for i in range(len_A + 1):
    for j in range(len_B + 1):
        if i == 0:
            DP[i][j] = j
        elif j == 0:
            DP[i][j] = i
        elif A[i - 1] == B[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + 1

print(DP[len_A][len_B])