#Estou usando dois 'if' pois quero que ele entre nos dois
#Se usasse apenas um 'if-elif' assim que o numero fosse par,
#nao seria verificado na condicional de baixo
#Podendo causar conflito em problemas onde eu quisesse saber se alem de 
#saber se o numero é par, quisesse saber se ele tbm é menor doq 10!
#EXEMPLO ABAIXO
#----
#TBM POSSO USAR APENAS USAR UM 'ELSE' NESSE
for numero in range(1,11):
  if numero % 2 == 0:
    print(f'O numero {numero} é par!')
  if numero % 2 == 1:
    print(f'O numero {numero} é impar!')


---------------------------------------------------------------------------


#Apenas os numero que nao entram na primeira condicional 
#sao verificados na segunda usando 'elif'!
#OUTRO EXEMPLO ABAIXO
for numero in range(1,11):
  if numero % 2 == 0:
    print(f'O numero {numero} é par!')
  elif numero < 10:
    print(f'O numero {numero} é menor do que 10!')


---------------------------------------------------------------------------


#EXEMPLO CORRETO!
for numero in range(1,11):
  if numero % 2 == 0:
    print(f'O numero {numero} é par!')
  if numero < 10:
    print(f'O numero {numero} é menor do que 10!')