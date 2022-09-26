import validador as val


def main():
    v = val.Validador()
    base_dados = []
    for i in range(0, 20):
        email = input("Informe email: ")
        if not v.check_email(email):
            print("Email invalido")

        else:
            entrada = {"Email": email}
            base_dados.append(entrada)
            print('email valido')


if __name__ == "__main__":
    main()
