#Caso eu quisesse facilitar e usar biblioteca: import math, e depois print(math.gcd(F1, F2))
N = int(input())
F = []
for i in range(N):
    F.append(input().split(" "))
    F1, F2 = int(F[i][0]), int(F[i][1])
    if F1>=F2:
        aux= F1
    elif F1<F2:
        aux= F2
    result = False
    while result is False:
        if F1 % aux == 0 and F2 % aux == 0:
            print(aux)
            result = True
        else:
            aux= aux -1