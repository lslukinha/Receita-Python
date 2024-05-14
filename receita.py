def add_receita(receitas_array):
    nome = input("Digite o nome da receita : ")
    pais_origem = input("Digite o país de origem da receita : ")
    ingredientes = input("Digite os ingredientes da receita separados por ';' : ")
    preparo = input("Digite o modo de preparo da receita separado por ';' : ")
    novaReceita = {"nome": nome,"pais_origem": pais_origem,"ingredientes": ingredientes.split(';'),"preparo": preparo.split(';')}
    receitas_array.append(novaReceita)
    print("Nova receita adicionada com sucesso!")
    print('asdf qwer')

def remove_receita(receitas_array):
    print("Receitas existentes:")
    visualizarReceitas(receitas_array)
    nome = input("Digite o nome da receita que deseja remover: ")
    for receita in receitas_array:
        if receita['nome'] == nome:
            receitas_array.remove(receita)
            print("Receita removida com sucesso!")
            return
    print("Não foi encontrada uma receita com esse nome.")


def visualizarReceitas(receitas_array):
    for receita in receitas_array:
        print(f"Nome: {receita['nome']}")
        print(f"Pais de origem: {receita['pais_origem']}")
        print("Ingredientes:", receita['ingredientes'])
        print("Preparo:", receita['preparo'])
        print()

def att_receita(receitas_array):
    print("Receitas existentes","\n")
    visualizarReceitas(receitas_array)
    nome = input("Digite da receita que vai ser atualizada : ")
    for receita in receitas_array:
        if receita['nome'] == nome:
            pais_origem = input("Digite o país de origem da receita: ")
            ingredientes = input("Digite os ingredientes da receita separados por ';' : ")
            preparo = input("Digite o modo de preparo da receita separado por ';' : ")
            receita["pais_origem"] = pais_origem
            receita["ingredientes"] = ingredientes.split(';')
            receita["preparo"] = preparo.split(';')
            print("Receita atualizada com sucesso!")
            return
        else:
            print("Não foi encontrada uma receita com esse nome.")

receitas_array = []

while True:
    print("\nMenu:")
    print("1- Adicionar receita")
    print("2- Atualizar")
    print("3- Filtrar país")
    print("4- Visualizar receitas")
    print("5- Excluir")
    escolha = input("Escolha a opção desejada(1-5): ")

    if escolha == "1":
        add_receita(receitas_array)

    elif escolha == "2":
        att_receita(receitas_array)

    elif escolha == "4":
        visualizarReceitas(receitas_array)

    elif escolha == "5":
        remove_receita(receitas_array)
    
    print()
