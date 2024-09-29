def imc (peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  print('---------------------------------------------------------------')
  print (f'O imc é de {meu_imc:.2f}')
  print("\n")
  if meu_imc < 18.5:
      print ('classificacao = "Magreza')
      print ('grau_obesidade = 0')
      print('---------------------------------------------------------------')
  elif 18.5 <= meu_imc < 25:
      print ('classificacao = "Normal"')
      print ('grau_obesidade = 0')
      print('---------------------------------------------------------------')
  elif 25 <= meu_imc < 30:
      print ('classificacao = "Sobrepeso"')
      print ('grau_obesidade = "I"')
      print('---------------------------------------------------------------')
  elif 30 <= meu_imc < 40:
      print ('classificacao = "Obesidade"')
      print ('grau_obesidade = "II"')
      print('---------------------------------------------------------------')
  else:
      print ('classificacao = "Obesidade Grave"')
      print ('grau_obesidade = "III"')
      print('---------------------------------------------------------------')
  
continuar = 1

while continuar == 1:

    print("\n")
    print('Bem vindo a calculador de IMC (Índice de massa corporal), deseja calcular?')
    continuar = int(input('Digite 1 para SIM e  0 para NÃO: '))

    if continuar == 0:
        print("\n")
        print('Fim da execução')
        print("\n")
        break
    else:
        continuar = 1

    print("\n")

    ps = float(input('Digite seu peso em kilos : '))

    print("\n")
    
    alt = float(input('Digite sua altura em metros (separanndo as casas por "."): '))
    
    print("\n")

    meu_imc = imc(ps, alt)

    print("\n")

    print('Deseja calcular mais uma vez?')
    continuar = int(input('Digite 1 para SIM e  0 para NÃO: '))
    if continuar == 0:
        print("\n")
        print('Fim da execução')
        print("\n")
        break
    else:
        continuar = 1