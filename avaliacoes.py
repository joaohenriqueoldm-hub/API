from pacientes import buscar_id, listar_pacientes

def id_avaliacao(avaliacoes):
    
    if len(avaliacoes) == 0:
        return 1
    
    maior = avaliacoes[0]["id"]

    for a in avaliacoes:

        if a["id"] > maior:
            maior = a["id"]
    
    return maior + 1


def cadastrar_avaliacao(pacientes, avaliacoes):
    listar_pacientes(pacientes)
    print("Escolha um Paciente para registrar uma avaliação")

    id = id_avaliacao(avaliacoes)
    id_paciente = buscar_id(pacientes)
    data = input("DATA: ")
    pressao = input("PRESSÃO: ")
    frequencia = int(input("FREQUÊNCIA CARDÍACA: "))
    observacao = input("OBSERVAÇÃO: ")

    avaliacao = {
        "id" : id,
        "paciente_id" : id_paciente,
        "data" : data,
        "pressao" : pressao,
        "frequencia" : frequencia,
        "observacao" : observacao
    }

    avaliacoes.append(avaliacao)


def listar_avaliacoes(pacientes, avaliacoes):
    listar_pacientes(pacientes)
    print("Escolha um Paciente para mostrar as avaliações")
    encontrados = []

    id_paciente = buscar_id(pacientes)

    for a in avaliacoes:
        if a["paciente_id"] == id_paciente:
            encontrados.append(a)
    
    for e in encontrados:
        print(f'AVALIAÇÕES DO PACIENTE ID Nº: {e["paciente_id"]}')
        print(f"""
    ID:         {e["id"]}
    DATA:       {e["data"]}
    PRESSÃO:    {e["pressao"]}
    FREQUÊNCIA: {e["frequencia"]}
    OBSERVAÇÃO: {e["observacao"]}
""")
    