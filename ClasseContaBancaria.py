class ContaBancaria:
    def __init__(self, titular, numero_conta):  # corrigido __init__
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} feito com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def exibir_extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo: R${self.saldo}")


# Testando a classe
conta1 = ContaBancaria("Isabela Fernandes", "26314789563")
conta1.depositar(3500)
conta1.sacar(250)
conta1.consultar_saldo()
conta1.exibir_extrato()
