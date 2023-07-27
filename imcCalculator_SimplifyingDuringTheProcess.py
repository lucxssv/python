def numero_quadrado(numero):
  quadrado = numero * numero
  return quadrado

def imc (peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada
  return meu_imc

meu_imc = imc(110, 1.85)
print(meu_imc)


---------------------------------------------------------------------------


def numero_quadrado(numero):
  quadrado = numero * numero
  return quadrado

def imc (peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada
  return meu_imc

meu_imc = imc(110, 1.85)
print(f'O meu imc é {meu_imc:.2f}')


---------------------------------------------------------------------------


def imc (peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  return meu_imc

meu_imc = imc(110, 1.85)
print(f'O meu imc é {meu_imc:.2f}')


---------------------------------------------------------------------------

simplifying
def imc (peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  print(f'O meu imc é {meu_imc:.2f}')
  return meu_imc

meu_imc = imc(110, 1.85)





