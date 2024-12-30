import random 
acertou = False 
valor_aleatorio = random.randint (1,10)
while acertou == False:
  numero = int (input ("Digite um número entre 1 e 10: "))
  if numero > valor_aleatorio:
    print ("O número chutado é maior que o número gerado")
  elif numero < valor_aleatorio:
    print ("O número chutado é menor que o número gerado ")
  elif numero == valor_aleatorio:
    acertou = True
    print ("Você acertou o número gerado! ")
    