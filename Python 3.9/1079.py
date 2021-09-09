qtd = int(input())
n = []
media = []
for i in range(qtd):
    n.append(input().split(" "))
    for j in range(3):
        n[i][j] = float(n[i][j])
        if j==0:
            n[i][j] = n[i][j] * 2
        elif j==1:
            n[i][j] = n[i][j] * 3
        elif j==2:
            n[i][j] = n[i][j] * 5
    media.append(sum(n[i]))
    print('{:.1f}'.format((media[i] / 10)))