lista = input().split(" ")
lados = []
aux=0;
for i in lista:
    lados.append(float(i))
lados.sort(reverse=True)

for i in lados:
    if lados.count(i)>aux:
        aux = lados.count(i)

if  lados[0] >=(lados[1]+lados[2]):
    print('NAO FORMA TRIANGULO')
else:
    if lados[0]**2 == (lados[1]**2 + lados[2]**2):
        print('TRIANGULO RETANGULO')
    if lados[0]**2 > (lados[1]**2 + lados[2]**2):
        print('TRIANGULO OBTUSANGULO')
    if lados[0]**2 < (lados[1]**2 + lados[2]**2):
        print('TRIANGULO ACUTANGULO')
    if aux==3:
        print('TRIANGULO EQUILATERO')
    if aux==2:
        print('TRIANGULO ISOSCELES')

