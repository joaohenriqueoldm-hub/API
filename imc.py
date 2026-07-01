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
        

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    classificacao = ""

    if imc <= 18.5:
        classificacao = "ABAIXO DO PESO"
    elif imc <= 24.9:
        classificacao = "PESO NORMAL"
    elif imc <= 29.9:
        classificacao = "SOBREPESO"
    elif imc >= 30:
        classificacao = "OBESIDADE"
    
    return classificacao


def mapear_imcs(pacientes):
    print("ID     NOME       IMC           CLASSIFICAÇÃO")
    for p in pacientes:
        print(f"{p["id"]}      {p["nome"]}      {p["imc"]:.2f}           {p["class_imc"]}")


def filtrar_imcs(pacientes):
    min = int(input("Mínimo: "))
    max = int(input("Máximo: "))

    encontrados = []

    for p in pacientes:
        if p["imc"] < max and p["imc"] > min:
            encontrados.append(p)
    
    listar_pacientes(encontrados)
        