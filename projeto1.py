fatorial = int(input("Digite um número: "))
n = 1
if fatorial > 0:
  for numero in range (1, fatorial + 1):
    n = n * numero
  print(f"O fatorial do número {fatorial} é {n}")
else:
  print("Número inválido")
