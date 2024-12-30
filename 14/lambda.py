#sukurkite fja kuri suskaiciuotu visu lyginiu indeksu reiksmiu suma

# import random
# def skaiciuGeneravimas(ilgis) :
#     skaiciai = []
#     for indeksas in range(ilgis) :
#         skaiciai.append(random.randint(5, 25))
#     return skaiciai
# skaiciai = skaiciuGeneravimas(4)
# print(skaiciai)


# def lyginiai(data, callback):
#     suma = 0
#     for i, sk in enumerate(data): 
#         suma += callback(i, sk)
#     return suma
    
# print(lyginiai(skaiciai, lambda i, sk : sk if i % 2 == 0 else 0))



# Jums duotas sąrašas su skaičiais: [-9, 25, 34, 2, 0]
# Neigiamus skaičius apgliaubkite laužtiniais skliaustais []
# 0 - ()
# Teigiamus - {}

# sarasas = [-9, 25, 34, 2, 0]

# print(list(map(lambda skaicius : f"[{skaicius}]" if skaicius < 0 else f"({skaicius})" if skaicius == 0 else f"{{{skaicius}}}", sarasas)))



# Duodamas sąrašas: [54 77 2 59 17 19 108]
# Pašalinkite iš jo visus skaičius kurie nėra pirminiai.
# Rezultatas: [2, 59, 17, 19]

listas  = [54, 77, 2, 59, 17, 19, 108]

print(list(filter(lambda sk: sk > 1 and all(sk % i != 0 for i in range(2, int(sk ** 0.5) + 1)), listas)))


