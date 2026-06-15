
# Primeiro exercicio
nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

ano_atual = 2026
idade = ano_atual - ano_nascimento

print(f"Olá '{nome}', você tem '{idade}' anos.")



# Segundo exercicio 
lado = float(input("Digite o tamanho do lado do quadrado: "))

area_quadrado = lado * lado

print(f"A área do quadrado é: {area_quadrado}")

# Terceiro exercicio
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area_retangulo = base * altura

print(f"A área do retângulo é: {area_retangulo}")

#Quarto Exercicio
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input(f"Digite a idade de {nome1}: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input(f"Digite a idade de {nome2}: "))

diferenca = (idade1 - idade2)

print(f"A diferença de idade entre {nome1} e {nome2} é de {diferenca} anos.")
