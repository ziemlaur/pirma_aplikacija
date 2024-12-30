

# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek 
# tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

# import random 
# skaiciai = []
# didesniUz150 = []
# didesniUz275 = []
# for i in range(300):
#     skaiciai.append(str(random.randint(0,300)))
#     if i > 150:
#         didesniUz150.append(str(i))
#     if i > 275:
#         didesniUz275.append(str(i))
# print('random skaiciai iki 300:')
# print(' '.join(skaiciai))
# print('didesni nei 150:')
# print(len(didesniUz150))
# print('didesni nei 275:')
# print(didesniUz275)


# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite 
# kableliais. Po paskutinio skaičiaus kablelio neturi būti.

dalinasi = []

for i in range(1, 3001):
    if i % 77 == 0:
        dalinasi.append(str(i))

print(','.join(dalinasi))




# Nupieškite tuščiavidurį kvadratą iš vartotojo įvedamo simbolio, kurio kraštinių kiekį taipogi leiskite įvesti vartotojui.

# simbolisS = input('Įveskite simbolį: ')
# kiekisS = int(input('Įveskite kiekį: '))

# for i in range(kiekisS):
#     if i == 0 or i == kiekisS - 1:  
#         print(simbolisS * kiekisS)
#     else: 
#         print(simbolisS + ' ' * (kiekisS - 2) + simbolisS)


# Nupieškite kvadratą iš vartotojo įvedamo simbolio, kurio kraštinių kiekį taipogi leiskite įvesti vartotojui.
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *


# simbolisS = input('iveskite simboli')
# kiekisS = int(input('iveskite kieki'))

# for i in range(1,kiekisS+1):
#     print(simbolisS*kiekisS)

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu. Simbolį paprašykite įvesti vartotojo.
# 5 * * * * * 5 
# * 5 * * * 5 * 
# * * 5 * 5 * * 
# * * * 5 * * *
# * * 5 * 5 * * 
# * 5 * * * 5 * 
# 5 * * * * * 5 

simbolisS = input('Įveskite simbolį: ')
kiekisS = int(input('Įveskite kiekį: '))
naujassimbolis = input('Įveskite simbolį, kurį naudosime įstrižainėms: ')

for i in range(kiekisS):
    eilute = ''
    for j in range(kiekisS):
        if i == j or j == kiekisS - 1 - i: 
            eilute += naujassimbolis
        else:
            eilute += simbolisS

 
    print(eilute)  

# Metam monetą. Monetos kritimo rezultatą imituojam randomint() funkcija, kur 0 yra herbas, o 1 - skaičius. 
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. 
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;


import random

1 scenarijus: monetos metimas sustabdomas iškritus herbui
while True:
    metimas = random.randint(0, 1)  
    if metimas == 0:
        print("H")  
        break
    else:
        print("S")  
print("metimas sustabdytas, iskrito herbas")


# 2 scenarijus: monetos metimas sustabdomas, kai herbai iškrenta tris kartus

# herbai = 0
# while herbai < 3:
#     metimas = random.randint(0, 1)  
#     if metimas == 0:
#         herbai += 1
#         print("H")  
#     else:
#         print("S")  
# print("Metimas sustabdytas, iškrito 3 herbai.")

# # 3 scenarijus: monetos metimas sustabdomas, kai herbai iškrenta tris kartus iš eilės
# herbai = 0
# while True:
#     metimas = random.randint(0, 1)  
#     if metimas == 0:
#         herbai += 1
#         print("H")  
#         if herbai == 3:
#             print("Metimas sustabdytas, iškrito 3 herbai iš eilės.")
#             break
#     else:
#         herbai = 0  
#         print("S")  


