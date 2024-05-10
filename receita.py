class Receita:
    def __init__(self, nome, pais_origem, ingredientes, preparo):
        self.nome = nome
        self.pais_origem = pais_origem
        self.ingredientes = ingredientes
        self.preparo = preparo

receitas = []

def visualizarReceitas(receitas):
    for receita in receitas:
        print(f"Nome: {receita.nome}")
        print(f"Pais de origem: {receita.pais_origem}")
        print(f"Ingredientes: {receita.ingredientes}")
        print(f"Preparo: {receita.preparo}")
        print()

while True:
    print("\nMenu:")
    print("1- Adicionar receita")
    print("2- Atualizar")
    print("3- Filtrar país")
    print("4- Visualizar receitas")
    print("5- Excluir")
    escolha = input("Escolha a opção desejada(1-5): ")

    if escolha == "1":
        nome = input("Qual o nome da receita?: ")
        pais_origem = input("Qual o país da receita?: ")
        ingredientes = input("Quais os ingredientes?: ")
        preparo = input("Qual modo de preparo?: ")
        novaReceita = Receita(nome, pais_origem, ingredientes, preparo)
        receitas.append(novaReceita)
    
    elif escolha == "4":
        visualizarReceitas(receitas)

