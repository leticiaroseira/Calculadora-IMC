def IMC(peso, altura):
  altura_quadrada = altura ** 2
  meu_IMC = peso / altura_quadrada
  print(f'O meu IMC é {meu_IMC:.2f}')
  return meu_IMC

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

meu_IMC = IMC(peso, altura)

