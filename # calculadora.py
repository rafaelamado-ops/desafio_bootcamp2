# calculadora.py

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

while True:
    print("\n=== CALCULADORA BÁSICA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '5':
        print("Encerrando...")
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        print("Resultado:", soma(n1, n2))
    elif opcao == '2':
        print("Resultado:", subtrai(n1, n2))
    elif opcao == '3':
        print("Resultado:", multiplica(n1, n2))
    elif opcao == '4':
        print("Resultado:", divide(n1, n2))
    else:
        print("Opção inválida!")
        