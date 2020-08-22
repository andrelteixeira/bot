import random

def getIntervalo(duracao, qtdAluno, chamada):
    total = (int(duracao) / (int(qtdAluno) * int(chamada)))
    return (int(total) * 60)

def chamaAluno(listaAluno):
    random.shuffle(listaAluno)
    return listaAluno

def funcname(parameter_list):
    pass