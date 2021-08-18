hi,mi,hf,mf = input().split(" ")
hi,mi,hf,mf = int(hi), int(mi), int(hf), int(mf)
if hf<=hi:
    h= hf- hi + 24
    if hf-hi==0 and  mf>mi:
        h=0
else:
    h= hf-hi

if mf<mi:
    m=mf-mi +60
    h= h-1
elif mf>=mi:
    m=mf-mi

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))