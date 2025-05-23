def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    3. print("Multiplicação") # Erro 1: Apenas o número da opção está errado.
    print("4. Divisão")

    while True:
        escolha = input("Digite sua escolha (1/2/3/4): ")

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Digite o primeiro número: ")) # Erro 2: Usando int() para números decimais
                num2 = int(input("Digite o segundo número: "))   # Erro 2: Usando int() para números decimais
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
                continue

            # Erro 3: Este é um erro de lógica mais sutil na formatação da saída.
            # O cálculo está correto, mas a apresentação pode ser enganosa.
            resultado = None # Inicializa resultado como None
            if escolha == '1':
                resultado = adicao(num1, num2)
            elif escolha == '2':
                resultado = subtracao(num1, num2)
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
            elif escolha == '4':
                resultado = divisao(num1, num2)
            
            print(f"O resultado é: {resultado}") # Erro 3 está aqui!

            proximo_calculo = input("Deseja fazer outro cálculo? (sim/não): ")
            if proximo_calculo.lower() != 'sim':
                break
        else:
            print("Escolha inválida. Por favor, digite 1, 2, 3 ou 4.")

calculadora()
