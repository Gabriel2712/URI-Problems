cod1, peca1, preco1 = input().split(" ")
cod2, peca2, preco2 = input().split(" ")

valor = (int(peca1) * float(preco1)) + (int(peca2) * float(preco2))

print('VALOR A PAGAR: R$ {:.2f}'.format(valor))