import re


class Validador(object):
    ##def __int__(self, email):
    ##   self.check_email()

    @staticmethod
    def check_email(email):
        regex = re.search(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$', email)

        if regex:

            return True

        else:

            return False

    @staticmethod
    def validatecpf(self: str) -> bool:
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', self):
            return False

            # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in self if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True




