di = input().split(" ")
di = di.pop()
hi, mi, si = input().split(":")
di, hi, mi, si = int(di), int(hi), int(mi), int(si)
df = input().split(" ")
df = df.pop()
hf, mf, sf = input().split(":")
df, hf, mf, sf = int(df), int(hf), int(mf), int(sf)

d = df - di
h = hf - hi
m = mf - mi
s = sf - si
if h < 0 or (h==0 and (m<0 or s<0)):
    d = d - 1
    h = h + 24

if m<0 or (m==0 and s<0):
    h = h - 1
    m = m + 60
if s<0:
    m = m - 1
    s = s + 60

print('{} dia(s)'.format(d))
print('{} hora(s)'.format(h))
print('{} minuto(s)'.format(m))
print('{} segundo(s)'.format(s))
