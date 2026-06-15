#Primiero exercicio
class ContaBancaria:
    def __init__(self, deposito_inicial):
        self.saldo = deposito_inicial

        if deposito_inicial <= 500:
            self.limite_cheque = 50
        else:
            self.limite_cheque = deposito_inicial * 0.5

        self.limite_original = self.limite_cheque
        self.divida_cheque = 0

    def consultar_saldo(self):
        print("\n===== EXTRATO =====")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Cheque Especial Disponível: R$ {self.limite_cheque:.2f}")
        print(f"Cheque Especial Máximo: R$ {self.limite_original:.2f}")

        if self.divida_cheque > 0:
            print(f"Valor utilizado do cheque especial: R$ {self.divida_cheque:.2f}")

    def consultar_cheque_especial(self):
        print(f"\nCheque especial disponível: R$ {self.limite_cheque:.2f}")

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        if self.divida_cheque > 0:
            taxa = self.divida_cheque * 0.20
            total_divida = self.divida_cheque + taxa

            print(f"Quitando dívida do cheque especial.")
            print(f"Taxa cobrada: R$ {taxa:.2f}")

            if valor >= total_divida:
                valor -= total_divida
                self.limite_cheque += self.divida_cheque

                if self.limite_cheque > self.limite_original:
                    self.limite_cheque = self.limite_original

                self.divida_cheque = 0
                self.saldo += valor
            else:
                print("Depósito insuficiente para quitar a dívida.")
                return
        else:
            self.saldo += valor

        print("Depósito realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        disponivel = self.saldo + self.limite_cheque

        if valor > disponivel:
            print("Saldo insuficiente.")
            return

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            restante = valor - self.saldo
            self.saldo = 0

            self.limite_cheque -= restante
            self.divida_cheque += restante

        print("Saque realizado com sucesso.")

    def pagar_boleto(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        disponivel = self.saldo + self.limite_cheque

        if valor > disponivel:
            print("Saldo insuficiente.")
            return

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            restante = valor - self.saldo
            self.saldo = 0

            self.limite_cheque -= restante
            self.divida_cheque += restante

        print("Boleto pago com sucesso.")

    def verificar_cheque_especial(self):
        if self.divida_cheque > 0:
            print(f"Usando R$ {self.divida_cheque:.2f} do cheque especial.")
        else:
            print("Não está utilizando cheque especial.")


print("=== ABERTURA DE CONTA ===")
deposito = float(input("Depósito inicial: R$ "))
conta = ContaBancaria(deposito)

while True:
    print("\n===== MENU =====")
    print("1 - Consultar saldo")
    print("2 - Consultar cheque especial")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Pagar boleto")
    print("6 - Verificar uso do cheque especial")
    print("7 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        conta.consultar_saldo()

    elif opcao == "2":
        conta.consultar_cheque_especial()

    elif opcao == "3":
        valor = float(input("Valor do depósito: R$ "))
        conta.depositar(valor)

    elif opcao == "4":
        valor = float(input("Valor do saque: R$ "))
        conta.sacar(valor)

    elif opcao == "5":
        valor = float(input("Valor do boleto: R$ "))
        conta.pagar_boleto(valor)

    elif opcao == "6":
        conta.verificar_cheque_especial()

    elif opcao == "7":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")

#Segundo exercicio
class Carro:
    def __init__(self):
        self.ligado = False
        self.velocidade = 0
        self.marcha = 0

    def ligar(self):
        if self.ligado:
            print("O carro já está ligado.")
        else:
            self.ligado = True
            print("Carro ligado.")

    def desligar(self):
        if not self.ligado:
            print("O carro já está desligado.")
        elif self.velocidade == 0 and self.marcha == 0:
            self.ligado = False
            print("Carro desligado.")
        else:
            print("O carro só pode ser desligado em ponto morto e velocidade 0 km/h.")

    def verificar_velocidade(self):
        print(f"Velocidade atual: {self.velocidade} km/h")
        print(f"Marcha atual: {self.marcha}")

    def acelerar(self):
        if not self.ligado:
            print("O carro está desligado.")
            return

        if self.marcha == 0:
            print("Não é possível acelerar em ponto morto.")
            return

        if self.velocidade >= 120:
            print("Velocidade máxima atingida.")
            return

        limite_superior = {
            1: 20,
            2: 40,
            3: 60,
            4: 80,
            5: 100,
            6: 120
        }

        if self.velocidade >= limite_superior[self.marcha]:
            print("Troque para uma marcha superior.")
            return

        self.velocidade += 1
        print(f"Velocidade: {self.velocidade} km/h")

    def diminuir_velocidade(self):
        if not self.ligado:
            print("O carro está desligado.")
            return

        if self.velocidade <= 0:
            print("O carro já está parado.")
            return

        self.velocidade -= 1
        print(f"Velocidade: {self.velocidade} km/h")

    def trocar_marcha(self, nova_marcha):
        if not self.ligado:
            print("O carro está desligado.")
            return

        if nova_marcha < 0 or nova_marcha > 6:
            print("Marcha inválida.")
            return

        if abs(nova_marcha - self.marcha) > 1:
            print("Não é permitido pular marchas.")
            return

        if nova_marcha == 0 and self.velocidade > 0:
            print("Não pode colocar em ponto morto com o carro em movimento.")
            return

        limites = {
            1: (0, 20),
            2: (21, 40),
            3: (41, 60),
            4: (61, 80),
            5: (81, 100),
            6: (101, 120)
        }

        if nova_marcha != 0:
            minimo, maximo = limites[nova_marcha]

            if self.velocidade < minimo or self.velocidade > maximo:
                print(
                    f"Velocidade incompatível com a marcha {nova_marcha}."
                )
                return

        self.marcha = nova_marcha
        print(f"Marcha alterada para {self.marcha}")

    def virar_esquerda(self):
        if not self.ligado:
            print("O carro está desligado.")
            return

        if 1 <= self.velocidade <= 40:
            print("Virando para a esquerda.")
        else:
            print("Só é possível virar entre 1 e 40 km/h.")

    def virar_direita(self):
        if not self.ligado:
            print("O carro está desligado.")
            return

        if 1 <= self.velocidade <= 40:
            print("Virando para a direita.")
        else:
            print("Só é possível virar entre 1 e 40 km/h.")


# MENU

carro = Carro()

while True:
    print("\n===== MENU CARRO =====")
    print("1 - Ligar carro")
    print("2 - Desligar carro")
    print("3 - Acelerar")
    print("4 - Diminuir velocidade")
    print("5 - Virar à esquerda")
    print("6 - Virar à direita")
    print("7 - Verificar velocidade")
    print("8 - Trocar marcha")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        carro.ligar()

    elif opcao == "2":
        carro.desligar()

    elif opcao == "3":
        carro.acelerar()

    elif opcao == "4":
        carro.diminuir_velocidade()

    elif opcao == "5":
        carro.virar_esquerda()

    elif opcao == "6":
        carro.virar_direita()

    elif opcao == "7":
        carro.verificar_velocidade()

    elif opcao == "8":
        try:
            marcha = int(input("Digite a nova marcha (0 a 6): "))
            carro.trocar_marcha(marcha)
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "9":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")

#Terceiro Exercicio
class MaquinaBanho:
    def __init__(self):
        self.agua = 0
        self.shampoo = 0
        self.pet = None
        self.pet_limpo = False
        self.precisa_limpeza = False

    def abastecer_agua(self):
        if self.agua + 2 <= 30:
            self.agua += 2
            print("2 litros de água adicionados.")
        else:
            print("Capacidade máxima de água atingida.")

    def abastecer_shampoo(self):
        if self.shampoo + 2 <= 10:
            self.shampoo += 2
            print("2 litros de shampoo adicionados.")
        else:
            print("Capacidade máxima de shampoo atingida.")

    def verificar_agua(self):
        print(f"Nível de água: {self.agua} litros")

    def verificar_shampoo(self):
        print(f"Nível de shampoo: {self.shampoo} litros")

    def verificar_pet(self):
        if self.pet:
            print(f"Pet na máquina: {self.pet}")
        else:
            print("Não há pet na máquina.")

    def colocar_pet(self, nome):
        if self.pet is not None:
            print("Já existe um pet na máquina.")
            return

        if self.precisa_limpeza:
            print("A máquina precisa ser limpa antes de receber outro pet.")
            return

        self.pet = nome
        self.pet_limpo = False
        print(f"{nome} foi colocado na máquina.")

    def dar_banho(self):
        if self.pet is None:
            print("Não há pet na máquina.")
            return

        if self.agua < 10:
            print("Água insuficiente.")
            return

        if self.shampoo < 2:
            print("Shampoo insuficiente.")
            return

        self.agua -= 10
        self.shampoo -= 2
        self.pet_limpo = True

        print(f"Banho realizado com sucesso em {self.pet}.")

    def retirar_pet(self):
        if self.pet is None:
            print("Não há pet para retirar.")
            return

        nome = self.pet

        if not self.pet_limpo:
            self.precisa_limpeza = True

        self.pet = None
        self.pet_limpo = False

        print(f"{nome} foi retirado da máquina.")

    def limpar_maquina(self):
        if self.agua < 3:
            print("Água insuficiente para limpeza.")
            return

        if self.shampoo < 1:
            print("Shampoo insuficiente para limpeza.")
            return

        self.agua -= 3
        self.shampoo -= 1
        self.precisa_limpeza = False

        print("Máquina limpa com sucesso.")


# MENU

maquina = MaquinaBanho()

while True:
    print("\n===== PET SHOP =====")
    print("1 - Dar banho")
    print("2 - Abastecer água")
    print("3 - Abastecer shampoo")
    print("4 - Verificar nível de água")
    print("5 - Verificar nível de shampoo")
    print("6 - Verificar pet na máquina")
    print("7 - Colocar pet na máquina")
    print("8 - Retirar pet da máquina")
    print("9 - Limpar máquina")
    print("10 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        maquina.dar_banho()

    elif opcao == "2":
        maquina.abastecer_agua()

    elif opcao == "3":
        maquina.abastecer_shampoo()

    elif opcao == "4":
        maquina.verificar_agua()

    elif opcao == "5":
        maquina.verificar_shampoo()

    elif opcao == "6":
        maquina.verificar_pet()

    elif opcao == "7":
        nome = input("Nome do pet: ")
        maquina.colocar_pet(nome)

    elif opcao == "8":
        maquina.retirar_pet()

    elif opcao == "9":
        maquina.limpar_maquina()

    elif opcao == "10":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")

    
