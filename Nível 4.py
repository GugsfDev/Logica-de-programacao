class Ingresso:
    def __init__(self, valor, filme, idioma):
        self.valor = valor
        self.filme = filme
        self.idioma = idioma

    def calcular_valor(self):
        return self.valor

    def exibir_ingresso(self):
        print("\n===== INGRESSO =====")
        print(f"Filme: {self.filme}")
        print(f"Idioma: {self.idioma}")
        print(f"Valor: R$ {self.calcular_valor():.2f}")


class MeiaEntrada(Ingresso):
    def calcular_valor(self):
        return self.valor / 2


class IngressoFamilia(Ingresso):
    def __init__(self, valor, filme, idioma, quantidade_pessoas):
        super().__init__(valor, filme, idioma)
        self.quantidade_pessoas = quantidade_pessoas

    def calcular_valor(self):
        total = self.valor * self.quantidade_pessoas

        if self.quantidade_pessoas > 3:
            total *= 0.95

        return total


while True:
    print("\n===== CINEMA =====")
    print("1 - Ingresso Normal")
    print("2 - Meia Entrada")
    print("3 - Ingresso Família")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        valor = float(input("Valor do ingresso: R$ "))
        filme = input("Nome do filme: ")
        idioma = input("Dublado ou Legendado: ")

        ingresso = Ingresso(valor, filme, idioma)
        ingresso.exibir_ingresso()

    elif opcao == "2":
        valor = float(input("Valor do ingresso: R$ "))
        filme = input("Nome do filme: ")
        idioma = input("Dublado ou Legendado: ")

        ingresso = MeiaEntrada(valor, filme, idioma)
        ingresso.exibir_ingresso()

    elif opcao == "3":
        valor = float(input("Valor do ingresso: R$ "))
        filme = input("Nome do filme: ")
        idioma = input("Dublado ou Legendado: ")
        pessoas = int(input("Quantidade de pessoas: "))

        ingresso = IngressoFamilia(
            valor,
            filme,
            idioma,
            pessoas
        )

        ingresso.exibir_ingresso()

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")

#sEGUNDO eXERCICIO
class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._logado = False

    # GETTERS E SETTERS
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_senha(self):
        return self._senha

    def set_senha(self, senha):
        self._senha = senha

    # MÉTODOS BASE
    def realizar_login(self):
        self._logado = True
        print(f"{self._nome} fez login.")

    def realizar_logoff(self):
        self._logado = False
        print(f"{self._nome} fez logoff.")

    def alterar_dados(self, nome=None, email=None):
        if nome:
            self._nome = nome
        if email:
            self._email = email
        print("Dados atualizados.")

    def alterar_senha(self, nova_senha):
        self._senha = nova_senha
        print("Senha alterada.")


# ---------------- GERENTE ----------------
class Gerente(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self._admin = True
        self._vendas = 0

    def gerar_relatorio_financeiro(self):
        print("Relatório financeiro gerado.")

    def consultar_vendas(self):
        print(f"Total de vendas registradas: {self._vendas}")


# ---------------- VENDEDOR ----------------
class Vendedor(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self._admin = False
        self._vendas = 0

    def realizar_venda(self):
        self._vendas += 1
        print("Venda realizada com sucesso.")

    def consultar_vendas(self):
        print(f"Total de vendas: {self._vendas}")


# ---------------- ATENDENTE ----------------
class Atendente(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self._admin = False
        self._caixa = 0.0

    def receber_pagamento(self, valor):
        if valor > 0:
            self._caixa += valor
            print(f"Pagamento recebido: R$ {valor:.2f}")

    def fechar_caixa(self):
        print(f"Valor final do caixa: R$ {self._caixa:.2f}")


# ---------------- MENU ----------------

usuarios = []

while True:
    print("\n===== SISTEMA DE USUÁRIOS =====")
    print("1 - Criar Gerente")
    print("2 - Criar Vendedor")
    print("3 - Criar Atendente")
    print("4 - Testar login")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        usuarios.append(Gerente(nome, email, senha))
        print("Gerente criado.")

    elif opcao == "2":
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        usuarios.append(Vendedor(nome, email, senha))
        print("Vendedor criado.")

    elif opcao == "3":
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        usuarios.append(Atendente(nome, email, senha))
        print("Atendente criado.")

    elif opcao == "4":
        if not usuarios:
            print("Nenhum usuário criado.")
            continue

        for i, u in enumerate(usuarios):
            print(f"{i} - {u.get_nome()}")

        idx = int(input("Escolha o usuário: "))
        usuarios[idx].realizar_login()
        usuarios[idx].realizar_logoff()

    elif opcao == "5":
        print("Encerrando sistema.")
        break

    else:
        print("Opção inválida.")

        #Terceiro Exercicio 
class Relogio:
 def __init__(self, hora=0, minuto=0, segundo=0):
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

def get_hora(self):
        return self._hora

def get_minuto(self):
        return self._minuto

def get_segundo(self):
        return self._segundo

def set_hora(self, hora):
        if 0 <= hora <= 23:
            self._hora = hora
        else:
            print("Hora inválida. Ajustada para 0.")
            self._hora = 0

def set_minuto(self, minuto):
        if 0 <= minuto <= 59:
            self._minuto = minuto
        else:
            print("Minuto inválido. Ajustado para 0.")
            self._minuto = 0

def set_segundo(self, segundo):
        if 0 <= segundo <= 59:
            self._segundo = segundo
        else:
            print("Segundo inválido. Ajustado para 0.")
            self._segundo = 0

        return f"{self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}"

def sincronizar(self, outro_relogio):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")


class RelogioBrasileiro(Relogio):
    def sincronizar(self, outro_relogio):
        self.set_hora(outro_relogio.get_hora())
        self.set_minuto(outro_relogio.get_minuto())
        self.set_segundo(outro_relogio.get_segundo())
        print("Relógio brasileiro sincronizado.")

class RelogioAmericano(Relogio):
    def set_hora(self, hora):
      
        if hora > 23 or hora < 0:
            print("Hora inválida. Ajustada para 0.")
            hora = 0

        if hora == 0:
            self._hora = 12
        elif 1 <= hora <= 12:
            self._hora = hora
        elif 13 <= hora <= 23:
            self._hora = hora - 12

    def sincronizar(self, outro_relogio):
        self.set_hora(outro_relogio.get_hora())
        self.set_minuto(outro_relogio.get_minuto())
        self.set_segundo(outro_relogio.get_segundo())
        print("Relógio americano sincronizado.")


relogio_br = RelogioBrasileiro()
relogio_us = RelogioAmericano()

while True:
    print("\n===== RELÓGIOS =====")
    print("1 - Definir horário brasileiro")
    print("2 - Definir horário americano")
    print("3 - Mostrar relógio brasileiro")
    print("4 - Mostrar relógio americano")
    print("5 - Sincronizar BR → US")
    print("6 - Sincronizar US → BR")
    print("7 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        h = int(input("Hora: "))
        m = int(input("Minuto: "))
        s = int(input("Segundo: "))
        relogio_br.set_hora(h)
        relogio_br.set_minuto(m)
        relogio_br.set_segundo(s)

    elif opcao == "2":
        h = int(input("Hora: "))
        m = int(input("Minuto: "))
        s = int(input("Segundo: "))
        relogio_us.set_hora(h)
        relogio_us.set_minuto(m)
        relogio_us.set_segundo(s)

    elif opcao == "3":
        print("BR:", relogio_br.mostrar_hora())

    elif opcao == "4":
        print("US:", relogio_us.mostrar_hora())

    elif opcao == "5":
        relogio_us.sincronizar(relogio_br)

    elif opcao == "6":
        relogio_br.sincronizar(relogio_us)

    elif opcao == "7":
        print("Encerrando sistema.")
        break

    else:
        print("Opção inválida.")
