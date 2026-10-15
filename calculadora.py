"""
Calculadora Básica
Operações: adição, subtração, multiplicação e divisão
Trabalho acadêmico — Compiladores
"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def exibir_menu():
    print("\n" + "=" * 30)
    print("       CALCULADORA BÁSICA")
    print("=" * 30)
    print("1 — Adição")
    print("2 — Subtração")
    print("3 — Multiplicação")
    print("4 — Divisão")
    print("5 — Sair")
    print("=" * 30)

def obter_numeros():
    while True:
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            return a, b
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "5":
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Escolha entre 1 e 5.")
            continue

        try:
            a, b = obter_numeros()

            if opcao == "1":
                resultado = somar(a, b)
                simbolo = "+"
            elif opcao == "2":
                resultado = subtrair(a, b)
                simbolo = "-"
            elif opcao == "3":
                resultado = multiplicar(a, b)
                simbolo = "×"
            elif opcao == "4":
                resultado = dividir(a, b)
                simbolo = "÷"

            # Exibe o resultado com formatação limpa
            if resultado == int(resultado):
                print(f"\nResultado: {a} {simbolo} {b} = {int(resultado)}")
            else:
                print(f"\nResultado: {a} {simbolo} {b} = {resultado:.2f}")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
