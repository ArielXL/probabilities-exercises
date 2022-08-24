def TuplaRepetida(tupleList,tuple):
    for i in tupleList:
        reversetuple = (tuple[1],tuple[0])
        if i == tuple or i == reversetuple:
            return True
    return False

def GrafosUnaArista():
    l = []
    for i in range(0, 5):
        for j in range(i + 1, 5):
            l.append((i,j))
    l.sort()
    return l

def GrafosDosAristas(l):
    result = []
    for i in range(0,len(l)):
        for j in range(i + 1,len(l)):
            x = [l[i],l[j]]
            x.sort()
            if not result.__contains__(x):
                result.append(x)
    return result

def GrafosNMasUnaAristas(nAristas,UnaArista):
    result = []
    for i in nAristas:
        for j in UnaArista:
            if not TuplaRepetida(i,j):
                l = []
                for k in i:
                    l.append(k)
                l.append(j)
                l.sort()
                if not result.__contains__(l):
                    result.append(l)
    return result

def GenerateGraph():

    result = []
    l = GrafosUnaArista()
    k = GrafosDosAristas(l)
    result.append(l)
    result.append(k)

    for i in range(0,8):
        k = GrafosNMasUnaAristas(k,l)
        result.append(k)
        i += 1

    return result
