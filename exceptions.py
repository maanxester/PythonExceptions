
class OperacacaoFinanceiraError(Exception):
    pass


class SaldoInsuficienteError(OperacacaoFinanceiraError):
    def __init__(self, message="", saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = "Saldo Insuficiente para efetuar a transacao\n" \
            f"Saldo Atual: {saldo}, Valor solicitado: {valor}"

        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg, self.saldo, *args)


