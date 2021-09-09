aux = 0
n = []
count = 0

while aux!=2:
    x = float(input())
    if x>=0 and x<=10:
        n.append(x)
        count = count +1
        if count==2:
            print('media = {:.2f}'. format(sum(n)/len(n)))
            while(aux!=1 and aux!=2):
                print('novo calculo (1-sim 2-nao)')
                aux = int(input())
            if aux==1:
                count=0
                n.clear()
                aux=0
    else:
        print('nota invalida')



