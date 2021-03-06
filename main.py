
from pprint import pprint
from exceptions import SaldoInsuficienteError, OperacacaoFinanceiraError
from leitor import LeitorDeArquivo


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitadas = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser um numero inteiro")

        if value <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo numero deve ser um numero inteiro")

        if value <= 0:
            raise ValueError("O atributo numero deve ser maior que zero")

        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo numero deve ser um numero inteiro")

        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O valor a ser sacado nao pode ser menor que zero")

        try:
            self.sacar(valor)
        except SaldoInsuficienteError as e:
            self.transferencias_nao_permitadas += 1
            e.args = ()
            raise OperacacaoFinanceiraError("Opera????o n??o finalizada") from e

        # Sintaxe raise <Exception> from e, lan??amos uma nova exce????o a partir de uma j?? tratada.

        # e.__context__ = SaldoInsuficienteError, podendo verificar o saldo e valor

        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser sacado nao pode ser menor que zero")
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError("", self.saldo, valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


def main():
    import sys

    contas = []
    while True:
        try:
            nome = input("Nome do cliente: \n")
            agencia = input("Numero da agencia: \n")
            numero = input("Numero da conta corrente: \n")

            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append = conta_corrente
        except KeyboardInterrupt:
            print(f"\n\n {len(contas)} conta(s) criadas")
            sys.exit()


# if __name__ == "__main__":
#     main()

# conta_corrente1 = ContaCorrente(None, 400, 1234567)
# conta_corrente2 = ContaCorrente(None, 401, 1234568)
#
# try:
#     conta_corrente1.transferir(1000, conta_corrente2)
#     print("Conta Corrente 1 Saldo: ", conta_corrente1.saldo)
#     print("Conta Corrente 2 Saldo: ", conta_corrente2.saldo)
#
# except OperacacaoFinanceiraError as e:
#     import traceback
#     traceback.print_exc()

# try:
#     leitor = LeitorDeArquivo("arquivo.txt")
#     leitor.ler_proxima_linha()
#
# # except IOError:
# #     print("Exce????o do tipo IOError capturada e tratada")
#
# finally:  # Finally sempre ser?? executado, mesmo ocorrendo exce????es
#     if 'leitor' in locals():  # Busca vari??veis localmente por todo o script
#         leitor.fechar()

with LeitorDeArquivo("arquivo.txt") as leitor:
    leitor.ler_proxima_linha()

