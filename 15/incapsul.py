import random

def skaiciuGeneravimas(ilgis):
    skaiciai = []
    for indeksas in range(ilgis):
        skaiciai.append(random.randint(5, 25))
    return skaiciai

bigList = []
for i in range(10):
    bigList.append(skaiciuGeneravimas(5))  

# print(bigList)


def didesniuUzDesimt(data):
    didesni = 0
    for skaicius in data:
            for y in skaicius:
                if y > 10 :
                 didesni += 1
    return didesni 
# print(didesniuUzDesimt(bigList))


def didziausias(data):
    sarasas = []
    a = 0
    for skaicius in data:
            for y in skaicius:
                if y > a:
                     sarasas.append(y)
                     a = y
                
    return max(sarasas)
   
# print(didziausias(bigList))


def indexuSuma(data):
    sumaPagalIndeksa = [0] * len(data[0])
    
    for mazasisSarasas in data:
        for indeksas, reiksme in enumerate(mazasisSarasas):
            sumaPagalIndeksa[indeksas] += reiksme

    return sumaPagalIndeksa


# print(indexuSuma(bigList))


def prideda7 (data):
    for i in data: 
         while len(i) < 7:
            i.append(random.randint(5, 25))
    
    return data

listas = prideda7(bigList)
# print(listas)
            

def sukuria(data):

    sumos = []
    for mazas in listas:
        sumos.append(sum(mazas))
    return sumos

# print(sukuria(listas))

            