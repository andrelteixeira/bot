def listaAluno():
    # abre o arquivo que contem a lista de alunos
    arq = open("arquivos/alunos.txt", 'r').readlines()
    listaAluno = []
    for aluno in arq:
        listaAluno.append(aluno.replace("\n", ""))
    
    return listaAluno


def LogChamada(msg):
    log = open("arquivos/log.txt", 'a')
    log.write(msg + "\n")

def iniciaArquivos():
    open("arquivos/log.txt", 'w')
    #open("arquivos/alunos.txt", 'w')