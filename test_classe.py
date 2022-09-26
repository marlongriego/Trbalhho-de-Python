import validador as val
import usavalidador


class TestEmail(object):

    def test_emailValido(self):
        result = val.Validador()
        email = 'marlongriego@gmail.com'
        assert result.check_email(email) == True

    def test_emailInvalido(self):
        result = val.Validador()
        email = 'marlongriegogmail.com'
        assert result.check_email(email) == False

    def test_emailValido2(self):
        result = val.Validador()
        email = 'marlongriego@ufam.eu.br'
        assert result.check_email(email) == True

    def test_cpfSemPonto(self):
        result = val.Validador
        cpf = '111.111.111-11'
        assert result.validatecpf(cpf) == False

    def test_cpfDigito2Errado(self):
        result = val.Validador()
        cpf = '010.303.622-92'
        assert result.validatecpf(cpf) == False

    def test_cpfDigito1Errado(self):
        result = val.Validador()
        cpf = '010.303.622-67'
        assert result.validatecpf(cpf) == False

    def test_cpf(self):
        result = val.Validador
        cpf = '010.303.622-97'
        assert result.validatecpf(cpf) == True

    def test_cpfNumvazio(self):
        result = val.Validador()
        cpf = ''
        assert result.validatecpf(cpf) == False
