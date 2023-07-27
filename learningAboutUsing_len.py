#'len' antes de 'notas' em 'quantidade' pega o tamanho da lista e divide por ele
#automatizando mais o codigo 
notas = [10, 8, 9, 7, 5]
quantidade = len(notas)
print('Quantidade de notas: ',quantidade)
soma = 0
for nota in notas:
  soma = soma + nota
print('A soma vale ',soma)
media = soma / quantidade
print('A média vale ',media) 