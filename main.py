import random
import string


def gerador():
    while True:
        print("Bem-Vindo Ao Gerador De Senhas")
        Alternativa = input("Você quer gerar uma senha: ".lower())
        Caracteres = int(input("Quantos Caracteres deseja:  "))
        especial = input("Você Deseja Caracteres Especiais:  ".lower())

        if Alternativa == "sim" and especial == "sim" and Caracteres > 0:
            senha = ""
            for _ in range(Caracteres):
                caracter = string.ascii_letters + string.digits + string.punctuation
                senha += random.choice(caracter)
            return senha
        elif Alternativa == "sim" and Caracteres > 0:
            senha = ""
            for _ in range(Caracteres):
                caracter = string.ascii_letters + string.digits
                senha += random.choice(caracter)
            return senha
        else:
            print("Não foi Gerada A Sua Senha")
        while True:
            opcao = input(
                "Deseja reiniciar (S/N)? "
            ).lower()  # converter para minúsculo
            if opcao not in ("s", "n"):
                print("opcao invalida, deve ser S ou N")
            elif opcao == "n":
                break  # sai do while interno, pois a opção é S ou N
            else:
                break


def Verificar(senha):
    leitor = len(senha)
    if leitor <= 6:
        return "Senha fraca"
    elif leitor <= 12:
        return "Senha Média"
    else:
        return "Senha Forte"


senha_gerada = gerador()
print(senha_gerada)
print(Verificar(senha_gerada))
