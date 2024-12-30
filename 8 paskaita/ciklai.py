#  1 uzduotis 

# simbolisS = input('iveskite simboli')
# kiekisS = int(input('iveskite kieki'))

# for i in range(1,kiekisS+1):
#     print(simbolisS*kiekisS)
# 

# Antra uzduotis

# miestai= ['Vilnius', 'Kaunas', 'Alytus', 'Rokiškis', 'Ūla', 'Mažeikiai', 'Akmena']
# for reiksme in miestai: 
#     if len(reiksme)>=6:
#         print(reiksme)


# trecia uzduotis

# simbolisegl = input('zvaigzdute ivesk : ')
# kiekisegl = int(input('kokia eglute: '))

# for i in range(1,kiekisegl+1):
#     print(simbolisegl*i)

#
#
#ketvirta uzduotis 

# t = 'Aš rytais mėgstu kavą su sumuštiniais ir arbata'
# index = 0

# for i in t:
#     if index %2==0:
#         print(i.upper(), index)
#     else: print(i.lower(), index)
#     index += 1

#isveskite tik tuos zodzius, kurie yra ilgesni nei nurodytas simboliu kiekis ir savyje turi nurodyta teksta. 
#ilgi ir teksta paraso zmogus


# listas = 'Aš rytais mėgstu kavą su sumuštiniais ir arbata'

# t = listas.split()
 

# tekstas = input('Tekstas: ')
# ilgis = int(input('Teksto ilgis: '))

# for zodis in t:
#     if len(zodis) > ilgis and tekstas in zodis:
#         print(zodis)

# isveskite teksta visa vienu metu kuriame kas antras zodis butu parasytas
# didziaja raide

# for indexas in range(len(t)):
#     if indexas %2 == 1:
#         t[indexas] = t[indexas].title()
# rezultatas  = ' '.join(t)
# print(rezultatas)


#isveskite teksta su kas ntuoju simboliu virsutiniame registre n iveda vartotojas

listas = 'Aš rytais mėgstu kavą su sumuštiniais ir arbata'

n = int(input('Įveskite n-tąjį skaičių: '))

rezultatas = ''
for indexas in range(len(listas)):
    if (indexas) % n == 1:  
        rezultatas += listas[indexas].upper()
    else:
        rezultatas += listas[indexas].lower()

print(rezultatas)


    




#                                           SARASU VEIKSMAI 
# 
# a = [1,2,3,4,5]
# b = [-7,-2,0,1,4]

# c = []
# d = []
# e = []
# for x , y in zip(a,b):
#     c += [x + y]
#     d += [x * y]
#     if y == 0:
#         print("cannot divide by zero")
#         e += [None]
#     else:
#         e += [x / y]
   

# print(f"c = {c},  d = {d}, e = {e} " )


                                # ARTIMETINIAI IR GEOMETRINIAI VIDURKIAI 

# while True:
#     n = int(input("iveskite sekos pradzios skaiciu: "))
#     k = int(input("iveskite sekos pabaigos skaiciu: "))
#     m = int(input("iveskite sekos zingsni: "))

#     seka = list(range(n, k + 1, m))

#     print(f"Sudarytas sąrašas: {seka}")
#     print(f"sekos suma = {(sum(seka))}")
#     print(f"sekos aritmetinis vidurkis = {(sum(seka)/len(seka))}")


#     sandauga = 1
#     for skaicius in seka:
#         sandauga *= skaicius

#     geometrinis_vidurkis = sandauga ** (1 / len(seka))

#     print(f"sekos geometrinis vidurkis = {geometrinis_vidurkis}")


#     testi = input("\nįveskite 'q' norėdami išeiti: ")
#     if testi.lower() == 'q':
#         print("skaiciavimas baigtas.")
#         break


#                                   teksto uzduotis 

t = "Vikipedija yra universali, daugiakalbė interneto enciklopedija, kaip bendruomeninis projektas, pagal viki technologiją ir pamatinius principus kuriama daugybės savanorių bei išlaikoma iš paaukotų lėšų"

# tekstas_su_didziaja =''

# for indexas, raide in enumerate(t):
#     if indexas % 2 == 0:
#         tekstas_su_didziaja += raide.upper()
#     else: tekstas_su_didziaja += raide
    
# print(tekstas_su_didziaja)




# tekstas_n = ''
# n = int(input("irasykite kas kelinta raide bus didzioji: "))

# for indexas, raide in enumerate(t):
#     if indexas % n == 0:
#         tekstas_n += raide.upper()
#     else: tekstas_n += raide

# print(tekstas_n)



# sarasas = t.split()
# zodziai_didziaja = []
# n = int(input("irasykite kas kelintas zodis bus didziaja: "))
# for indexas, zodis in enumerate(sarasas):
#     if indexas % n == 0:
#         zodziai_didziaja.append(zodis.upper())
#     else: 
#         zodziai_didziaja.append(zodis)

# print(" ".join(zodziai_didziaja))



# sarasas = t.split()
# zodziai_didziosiomis_raid = []

# for i in sarasas:
#     zodziai_didziosiomis_raid.append(i.title())
# print(" ".join(zodziai_didziosiomis_raid))


