#Primeiro Exercicio
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"\n--- Tabuada do {numero} ---")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Segundo exercicio
peso = float(input("Digite seu peso (em kg, ex: 70.5): "))
altura = float(input("Digite sua altura (em metros, ex: 1.75): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc <= 18.5:
    print("Classificação: Abaixo do peso")
elif imc <= 24.9:
    print("Classificação: Peso ideal")
elif imc <= 29.9:
    print("Classificação: Levemente acima do peso")
elif imc <= 34.9:
    print("Classificação: Obesidade Grau I")
elif imc <= 39.9:
    print("Classificação: Obesidade Grau II (Severa)")
else:
    print("Classificação: Obesidade III (Mórbida)")

#Terceiro Exercicio
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número (deve ser MAIOR que o primeiro): "))

while num2 <= num1:
    num2 = int(input("Inválido. O segundo número DEVE ser maior que o primeiro: "))

print("\nEscolha uma opção:")
print("1 - Par")
print("2 - Ímpar")
opcao = input("Digite 1 ou 2: ")

resto_desejado = 0 if opcao == "1" else 1
tipo_texto = "pares" if opcao == "1" else "ímpares"

print(f"\nNúmeros {tipo_texto} entre {num2} e {num1} (decrescente):")

for i in range(num2, num1 - 1, -1):
    if i % 2 == resto_desejado:
        print(i, end=" ")
print() 

#Quarto exercicio
num_inicial = int(input("Digite o número inicial (divisor base): "))

while num_inicial == 0:
    num_inicial = int(input("O número inicial não pode ser 0. Digite outro: "))

print("\nO programa continuará pedindo números.")
print(f"Regra: Números menores que {num_inicial} serão ignorados.")
print(f"O programa para se o número digitado NÃO for divisível por {num_inicial}.\n")

while True:
    num_atual = int(input("Digite um número: "))
    
    if num_atual < num_inicial:
        print(f"-> {num_atual} é menor que {num_inicial}. Ignorado.")
        continue 
     
    if num_atual % num_inicial != 0:
        print(f"\n-> Execução interrompida! {num_atual} dividido por {num_inicial} deixa resto {num_atual % num_inicial} (diferente de 0).")
        break
        
    print(f"-> {num_atual} é divisível por {num_inicial}. Continuando...")
