A, B, C = input().split(" ")
A, B, C = float(A), float(B), float(C)

if A>=B+C or B>= A+C or C>=A+B:
    print('Area = {:.1f}'.format((A + B) / 2 * C))
else:
    print('Perimetro = {:.1f}'.format(A + B + C))


