import arquivo
import aula
import time

arquivo.iniciaArquivos()

print("Para iniciar o sistema é necessario informar a lista de aluno!!\n\n")
print("Por favor, coloque os nomes na caminho 'arquivos/alunos.txt'!!")
importaAluno = input("Você já importou a lista de alunos?(s/n): ")

if (importaAluno == "s"):
    alunos = arquivo.listaAluno()

    #realiza os inputs
    duracao = input("Digite o tempo de aula: ") # duração da aula
    chamada = input("Digite a quantidade de chamadas a serem feitas: ") # quantidade de vezes que o mesmo nome será chamado

    # gera o intervalo entre as chamadas
    intervalo = aula.getIntervalo(duracao, chamada, len(alunos))

    # gera a ordem de chamada
    listaChamada = [] 
    i = 0
    # unifica todas as chamadas em uma unica lista
    while (i < int(chamada)):
        listaChamada = listaChamada + aula.chamaAluno(alunos.copy())
        i += 1

    #realiza a chamada entre o intervalo predefinido
    for chamando in listaChamada:
        msg = "Atenção: o aluno (a) " + chamando.upper() + " está presente? (s/n)"
        rsp = input(msg)
        arquivo.LogChamada(msg + rsp)
        time.sleep(intervalo)