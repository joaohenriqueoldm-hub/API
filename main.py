from pacientes import cadastrar_pacientes, listar_pacientes, atualizar_paciente, remover_paciente, buscar_pacientes
from avaliacoes import cadastrar_avaliacao, listar_avaliacoes

pacientes = []
avaliacoes = []

while True:
    print("""
=================================================
VIDAFIT - AVALIACAO DE SAUDE
=================================================
1. Cadastrar paciente
2. Listar pacientes
3. Atualizar paciente
4. Remover paciente
5. Cadastrar avaliacao (vincular a um paciente)
6. Listar avaliacoes de um paciente
7. Buscar paciente por nome
8. Ordenar pacientes (idade / peso / IMC)
9. Calcular IMC de todos (map)
10. Filtrar pacientes por faixa de IMC (filter)
11. Estatisticas gerais (reduce)
0. Sair
=================================================
""")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_pacientes(pacientes)
    elif opcao == 2:
        listar_pacientes(pacientes)
    elif opcao == 3:
        atualizar_paciente(pacientes)
    elif opcao == 4:
        remover_paciente(pacientes)
    elif opcao == 5:
        cadastrar_avaliacao(pacientes, avaliacoes)
    elif opcao == 6:
        listar_avaliacoes(pacientes, avaliacoes)
    elif opcao == 7:
        buscar_pacientes(pacientes)
    
        


