import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Por favor, digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano de nascimento fora do intervalo válido.")
        except ValueError:
            print("Por favor, digite um valor numérico para o ano de nascimento.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome = input("Por favor, digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)

    print(f"Olá, {nome}!")
    print(f"Você tem ou completará {idade} anos em 2022.")

if __name__ == "__main__":
    main()
