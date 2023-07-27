def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('O aluno tirou', media)
  return media

def verificar_aprovacao(media):
  if media >= 6:
    print('Aluno Aprovado :)')
  else:
    print('Aluno Reprovado :( ')

lucas = [8, 10, 9, 10]
media = calcular_media(lucas)
verificar_aprovacao(media)