def id_paciente(pacientes):

    if len(pacientes) == 0:
        return 1
    
    maior = pacientes[0]["id"]

    for p in pacientes:

        if p["id"] > maior:
            maior = p["id"]
    
    return maior + 1


def cadastrar_pacientes(pacientes):

    id = id_paciente(pacientes)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M) ou (F): ")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))

    paciente = {
        "id" : id,
        "nome" : nome,
        "idade" : idade,
        "sexo" : sexo,
        "peso" : peso,
        "altura" : altura
    }

    pacientes.append(paciente)


def listar_pacientes(pacientes):
    if len(pacientes) == 0:
        return "Não há Pacientes Registrados"
    
    for paciente in pacientes:
        print(f"""
    ID: {paciente["id"]}
    NOME: {paciente["nome"]}
    IDADE: {paciente["idade"]}
    SEXO: {paciente["sexo"]}
    PESO: {paciente["peso"]}
    ALTURA: {paciente["altura"]}
""")
        

def buscar_id(pacientes):

    id_buscado = int(input("Digite o ID: "))

    for p in pacientes:

        if p["id"] == id_buscado:
            return p["id"]
        else:
            print("ID não encontrado")


def atualizar_paciente(pacientes):
    id_buscado = buscar_id(pacientes)
    for p in pacientes:
        if p["id"] == id_buscado:
            print("Paciente Encontrado")
            print()
            print("Digite as Informações Novamente para mantê-las as mesmas")
            print()

            nome = input(f'NOME ({p["nome"]}): ')
            idade = int(input(f'IDADE ({p["idade"]}): '))
            sexo = input(f'SEXO ({p["sexo"]}): ')
            peso = float(input(f'PESO ({p["peso"]}): '))
            altura = float(input(f'ALTURA ({p["altura"]}): '))

            if nome != "":
                p["nome"] = nome
            if idade != None:
                p["idade"] = idade
            if sexo != "":
                p["sexo"] = sexo
            if peso != None:
                p["peso"] = peso
            if altura != None:
                p["altura"] = altura

            print("Cadastro do Paciente Atualizado com Sucesso")
        


def remover_paciente(pacientes):
    id_buscado = buscar_id(pacientes)
    resposta = input(f"Deseja mesmo remover o paciente de ID Nº: {id_buscado}? ")
    if resposta == "SIM":
        for p in range(len(pacientes)):

            if pacientes[p]["id"] == id_buscado:

                pacientes.pop(p)

                print("Paciente Removido com Sucesso")
        else:
            print()


def buscar_pacientes(pacientes):
    encontrados = []
    termo = input("Digite o Nome: ")
    for p in pacientes:
        if termo.lower() in p["nome"].lower():
            encontrados.append(p)
    listar_pacientes(encontrados)