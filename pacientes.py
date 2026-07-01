from imc import calcular_imc, classificar_imc
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
    imc = calcular_imc(peso, altura)
    class_imc = classificar_imc(imc)

    paciente = {
        "id" : id,
        "nome" : nome,
        "idade" : idade,
        "sexo" : sexo,
        "peso" : peso,
        "altura" : altura,
        "imc" : imc,
        "class_imc" : class_imc
    }

    pacientes.append(paciente)


def listar_pacientes(pacientes):
    if len(pacientes) == 0:
        return "Não há Pacientes Registrados"
    
    for paciente in pacientes:
        print(f"""
    ID:            {paciente["id"]}
    NOME:          {paciente["nome"]}
    IDADE:         {paciente["idade"]}
    SEXO:          {paciente["sexo"]}
    PESO:          {paciente["peso"]}
    ALTURA:        {paciente["altura"]}
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
            imc = calcular_imc(peso, altura)
            class_imc = classificar_imc(imc)

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
            if peso != None and altura != None:
                p["imc"] = imc
                p["class_imc"] = class_imc

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


def ordenar_pacientes(pacientes):

    print("1 - IDADE")
    print("2 - PESO")
    print("3 - IMC")

    opcao = input("Escolha: ")

    ordem = input("ASC ou DESC: ").upper()

    if ordem == "DESC":
        reverse = True
    else:
        reverse = False

    if opcao == "1":
        lista = sorted(pacientes,
                       key=lambda x: x["idade"],
                       reverse=reverse)

    elif opcao == "2":
        lista = sorted(pacientes,
                       key=lambda x: x["peso"],
                       reverse=reverse)

    elif opcao == "3":
        lista = sorted(pacientes,
                       key=lambda x: x["imc"],
                       reverse=reverse)

    else:
        print("Opção inválida.")
        return

    listar_pacientes(lista)


def calcular_imc_medio(pacientes):
    soma = 0

    for p in pacientes:
        imc = p["imc"]
        soma += imc

    media = soma / len(pacientes)

    return media


def contar_por_faixa_imc(pacientes):
    contador = 0 

    for p in pacientes:
        if p["class_imc"] == "SOBREPESO" or p["class_imc"] == "OBESIDADE":
            contador += 1

    return contador


def estatisticas(pacientes):
    imc_medio = calcular_imc_medio(pacientes)
    pacientes_s_o = contar_por_faixa_imc(pacientes)

    print(f"""
   --- ESTATISTICAS GERAIS (REDUCE) ---
Total de pacientes cadastrados: {len(pacientes)}
IMC medio da base..............: {imc_medio:.2f}
Pacientes com sobrepeso/obesidade: {pacientes_s_o}
------------------------------------------------
""")
