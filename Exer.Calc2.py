def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == '0':
            print("Obrigado por usar a calculadora. Até mais!")
            break
        elif opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = num1 + num2
            print("Resultado:", resultado)
        elif opcao == '2':
            resultado = num1 - num2
            print("Resultado:", resultado)
        elif opcao == '3':
            resultado = num1 * num2
            print("Resultado:", resultado)
        elif opcao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero.")
            else:
                resultado = num1 / num2
                print("Resultado:", resultado)

calculadora()
