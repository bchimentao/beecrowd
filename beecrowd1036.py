# 1036 - Fórmula de Bhaskara

A, B, C = map(float, input().split(' '))

delta = B**2 - (4 * A * C)
R1 = 0
R2 = 0

if A == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
elif delta == 0:
    R1 = -B / (2 * A)
    R2 = R1
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    R1 = (-B + delta**(1/2)) / (2 * A)
    R2 = (-B - delta**(1/2)) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")