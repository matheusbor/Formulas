c = 2.99792458e8
h = 6.62607015e-34
v = None 
f = None #às vezes precisamos representar frequência com f
comprimento_onda = None # λ = c / v    ou     λ = v / f
E = None # h * v

operação = int(input(''' 
Qual operação deseja fazer?
[1] Calcular o comprimento de onda
[2] Calcular a energia de um fóton
'''))

def calcular_comprimento_onda():
    onda = input("É radiação eletromagnética? (s para sim e n para não): ")
    if onda == "s":
        print("\nEscreva com a precisão que quiser:")
        v = float(input("Qual a frequência da onda? "))
        comprimento_onda = c / v
        print("O comprimento desta onda é: ",comprimento_onda)
    else:
        print("\nEscreva com a precisão que quiser:")
        v = float(input("Qual a velocidade da onda? "))
        f = float(input("Qual a frequência da onda? "))
        comprimento_onda = v / f
        print("O comprimento desta onda é: ",comprimento_onda)

def calcular_energia_foton():
    v = float(input("Qual a frequência da onda? "))
    E = h * v
    print("A energia deste fóton é: ",E)

def escolher_operacao(operação):
    switcher = {
        1: calcular_comprimento_onda,
        2: calcular_energia_foton
    }
    func = switcher.get(operação, lambda: print("Opção inválida"))
    func()

escolher_operacao(operação)
