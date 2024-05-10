arquivo = open("receitas.csv", "w" )
class Receita:
    def _init_(self, nome, pais_origem, ingredientes, preparo):
        self.nome = nome
        self.pais_origem = pais_origem
        self.ingredientes = ingredientes
        self.preparo = preparo

receitas = []

def visualizarReceita(receitas):
    for receita in receitas:
        print(f"Nome {nome}")
        print(f"Pais de origem {pais_origem}")
        print(f"Ingredientes {ingredientes}")
        print(f"Preparo {preparo}")

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
        print(visualizarReceita)
