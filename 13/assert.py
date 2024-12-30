# duomenys = [
#     {
#         "pavadinimas": "3-jų lentynų komplektas Tobi 3P, baltas",
#         'kaina': 12,
#         "ivertinimas": 3.7
#     },
#     {
#         "pavadinimas": "Pakabinama sieninė lentyna Bilbao 4P, balta matinė",
#         "kaina": 508.22,
#         "ivertinimas": 4.8
#     },
#     {
#         "pavadinimas": "Lentyna R60, balta",
#         "kaina": 47.41,
#         "ivertinimas": 2.5
#     }
# ]

# def patikrinimas(duomenys):
#     global bendra_kaina
#     global vidutinis_ivertinimas
#     bendra_kaina = 0
#     ivertinimu_suma = 0
#     produktu_skaicius = len(duomenys)

#     for produktas in duomenys:
    
#         assert 'pavadinimas' in produktas, "Trūksta pavadinimo"
#         assert 'kaina' in produktas, "Trūksta kainos"
#         assert 'ivertinimas' in produktas, "Trūksta ivertinimo"
        
#         bendra_kaina += produktas['kaina']
#         ivertinimu_suma += produktas['ivertinimas']
    
#     vidutinis_ivertinimas = ivertinimu_suma / produktu_skaicius

# patikrinimas(duomenys)
# print(f"Bendra kaina: {bendra_kaina}")
# print(f"Vidutinis įvertinimas: {vidutinis_ivertinimas}")


import random
def skaiciuGeneravimas(ilgis) :
    skaiciai = []
    for indeksas in range(ilgis) :
        skaiciai.append(random.randint(5, 25))
    return skaiciai
skaiciai = skaiciuGeneravimas(7)


print(skaiciai)


def daugiauUzDesimt(data):
    counter = 0
    for skaicius in data:
        if skaicius > 10:
            counter += 1

    return counter

counter = daugiauUzDesimt(skaiciai)

# print(counter)

     


def didziausias(data):
    max_value = max(data) 
    max_indexes = []
    
    for index, value in enumerate(data):
        if value == max_value:
            max_indexes.append(index)
    return max_value, max_indexes

max_value, max_indexes = didziausias(skaiciai)

# print("Generated list:", skaiciai)
# print("Maximum value:", max_value)
# print("Indexes of maximum value:", max_indexes)



def lyginiai(data):
    suma = 0

    for i, sk in enumerate(data): 
        if i %2 == 0:       
            suma += sk
    return suma 
suma = lyginiai(skaiciai)
# print(suma)


def minusIndex(data):
    listas = []
    for index, number in enumerate(data):

        listas.append(number-index)
    return listas 
listas = minusIndex(skaiciai)
# print(listas)



def duSarasai(data, uni = None):
    listas1 = []
    listas2 = []
    for i, sk in enumerate(data): 
        if i %2 == 0:       
            listas1.append(sk)
        else:
            listas2.append(sk)
    if uni == 'U':
        listas1 = set(listas1)
        listas2 = set(listas2)
    
    return listas1, listas2
sarasai = duSarasai(skaiciai,'U')
# print(sarasai)


def poriniaiIndexai(data):
    listas = []
    for i, sk in enumerate(data): 
        if i %2 == 0 and sk >= 15:       
            listas.append(0)
        else:
            listas.append(sk)
    return listas 

listas = poriniaiIndexai(skaiciai)
# print(listas)


def parametrai(*data, daugiau=None):
    for i, sk in enumerate(data):
        if sk > 10:
            print(i)
            break
   
    listas = []
    if 'D' in daugiau:
        for i, sk in enumerate(data):
            if sk > 10:
                listas.append(i)
    
    return listas
indexas = parametrai(1, 2, 3, 'D')
print(indexas)

