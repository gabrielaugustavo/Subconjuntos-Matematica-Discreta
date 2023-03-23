def produto_cartesiano(conj): # faz o estabelecimento de cada possibilidade de conjunto
    resultado = []
    for i in conj:
        for j in conj:
            resultado += [[i,j]]
    return resultado

def partes_de_conj(p, n): # analisa e define as partes do conjunto
  r = []
  for aux in range(2**(len(p))): 
    r.append([])
    i = 0
    while(len(p) > i):
      if(aux & 2**i > 0):
        r[aux].append(p[i])
      i += 1
    classe = classifica(aux,n)
    resultado = str(r[aux]) + classe + "\n" #salva o resultado com a respectiva classificacao
    arq.write(resultado)
  return None

def par(i, j, rel, n): 
    return 1<<i*n + j & rel == 1<<i*n + j

def classifica(rel, n): #faz a classificação de cada subconjunto
    classe = ""
    if(reflexiva(rel,n)):
        classe += 'R'
    if(simetrica(rel, n)):
        classe += "S"
    if(transitiva(rel, n)):
        classe += "T"
    if(irreflexiva(rel, n)):
        classe += "I"
    if(antissimetrica(rel, n)):
        classe += "As"
    if "R" in classe and "S" in classe and "T" in classe:
        classe += "E"
    if(funcao(rel, n) and rel != 0) :
        classe += "Fu"
        if injetora(rel, n) and sobrejetora(rel, n):
            classe += "FbFiFs"
        elif injetora(rel, n):
            classe += "Fi"
        elif sobrejetora(rel, n):
            classe += "Fs"
    return classe

def reflexiva(rel, n):
    for x in range(n):
        if not(par(x,x,rel,n)):
            return False
    return True

def simetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and not par(j, i, rel, n):
                return False
    return True

def transitiva(rel, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if par(i, j, rel, n) and par(j, k, rel, n) and not par(i, k, rel, n):
                    return False
    return True

def irreflexiva(rel, n):
    for i in range(n):
        if par(i, i, rel, n):
            return False
    return True

def antissimetrica(rel, n):
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n) and par(j, i, rel, n) and not i == j:
                return False
    return True

def funcao(rel, n):
    aux = 0
    for i in range(n):
        for j in range(n):
            if par(i, j, rel, n):
                aux += 1
        if aux == 0 or  aux > 1:
            return False
        aux = 0
    return True

def injetora(rel, n):
    aux = 0

    for i in range(n):
        for j in range(n):
            if par(j, i, rel, n) and aux < 1:
                aux += 1
            elif(par(j, i, rel, n)):
                return False
        aux = 0
    return True

def sobrejetora(rel , n):
    aux = False

    for i in range(n):
        for j in range(n):
            if par(j, i, rel, n):
                aux = True
                continue
        if not aux:
            return False
        aux = False

    return True

def lista(): # cria uma lista com elementos inseridos no input
    lista = []
    elem = int(input("Insira o total de elementos no conjunto desejado:"))
    for i in range (elem):
            lista.append((i)+1)

    return lista

arq = open("subconjuntos", "w")
import time 
antes = time.time() # faz a contagem do tempo
r = lista()   
p = produto_cartesiano(r)
partes_de_conj(p,len(r))
arq.close()
depois = time.time()
print(depois - antes)
