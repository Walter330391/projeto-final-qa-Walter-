#teste03
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
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite sua escolha (1/2/3/4): ")

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Digite o primeiro número: ")) # Erro 1: Usando int() para números decimais
                num2 = int(input("Digite o segundo número: "))   # Erro 1: Usando int() para números decimais
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
                continue

            if escolha == '1':
                print(f"{num1} + {num2} = {adicao(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {divisao(num1, num2)}")
            
            # Erro 2 (novo): Este erro afetará o fluxo de saída da calculadora.
            proximo_calculo = input("Deseja fazer outro cálculo? (sim/não): ")
            if proximo_calculo.lower() == 'sim': # O erro está aqui!
                continue # Continua o loop sem pedir nova entrada para a operação.
            else:
                break
        else:
            print("Escolha inválida. Por favor, digite 1, 2, 3 ou 4.")

calculadora()
