
class SaldoInsuficienteError(Exception):
    def __int__(self, message="", saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = "Saldo Insuficiente para efetuar a transacao\n" \
            f"Saldo Atual: {saldo}, Valor a ser sacado: {valor}"

        super(SaldoInsuficienteError, self).__init__(message or msg, self.saldo, *args)
