c = 2.99792458e8
h = 6.62607015e-34

def calcular_comprimento_onda():
    onda = input("É radiação eletromagnética? (s para sim e n para não): ")
    if onda == "s":
        v = float(input("Qual a frequência da onda? "))
        comprimento_onda = c / v
    else:
        v = float(input("Qual a velocidade da onda? "))
        f = float(input("Qual a frequência da onda? "))
        comprimento_onda = v / f
    print("O comprimento desta onda é: ", comprimento_onda)

def calcular_energia_foton():
    v = float(input("Qual a frequência da onda? "))
    E = h * v
    print("A energia deste fóton é: ", E)

opcoes = {
    1: calcular_comprimento_onda,
    2: calcular_energia_foton,
}

opcao = int(input(''' 
Qual operação deseja fazer?
[1] Calcular o comprimento de onda
[2] Calcular a energia de um fóton
'''))

funcao_selecionada = opcoes.get(opcao)
if funcao_selecionada:
    funcao_selecionada()
else:
    print("Opção inválida")
