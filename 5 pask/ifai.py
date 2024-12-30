# amzius = int(input('Įveskite amziu'))
# if amzius>=18:
#     print ('gali balsuot')


# pirmas = int(input('Įveskite pazymi'))
# antras = int(input('Įveskite pazymi'))
# trecias = int(input('Įveskite pazymi'))

# vidurkis = ((pirmas+antras+trecias)/3)
# if vidurkis >=5:
#     print('vidurkis teigiamas')


# a = 13
# if a%5 == 0:
#     print (a*1)
#     print (a*2)
#     print (a*3)
#     print (a*4)
#     print (a*5) 
# elif a%2 == 0:
#     print(a)
#     print(a**2)
#     print(a**2/2)
# elif a%7 != 0:
#     b = 20
#     print(b+7)
#     print(b-7)

    

# skaicius = (int(input ('skaicius nr 1')))
# skaiciusS = (int(input ('skaicius nr 2')))

# if skaicius > skaiciusS:
#     print ('pirmas didesnis')
# elif skaicius < skaiciusS :
#     print ('antras didesnis')
# else: print ('jie lygus')

# tekstas = (input('iveskit teksta'))
# sakinys = 'Vilnius yra UNESCO paveldas nuo 1996 metu.'

# if sakinys.find(tekstas)>=0:
#     print('tekstas yra sakinyje')
# else:
#     print ('teksto ner')



# skaicius = (input ('skaicius'))
# if skaicius.isnumeric():
#     skaicius = int(skaicius) 
#     if skaicius >=10 and skaicius <=20:
#         print (str(skaicius) + ' skaicius yra tarp 10 ir 20')
#     else: print('skaicius nera tarp 10 ir 20')
# else: print('ivesk skaiciu')

# skaicius = (int(input ('skaicius')))
# if skaicius%2==0:
#     print('lyginis')
# else: print('nelyginis')

# skaicius = (int(input ('skaicius')))
# if skaicius%3==0:
#     print ('fizz')
# elif skaicius%5==0:
#     print('buzz')
# elif skaicius%5==0 and skaicius%3==0:
#     print('fizzbuzz')
# else: print(skaicius)


# tekstas = (input('iveskit teksta'))
# if tekstas:
#     print('ivesta')
# if tekstas.isnumeric():
#     print('skaiciai')
# elif tekstas.isalpha():
#     print('tik teksts')
#     if tekstas.isupper():
#         print("Tekstas parašytas didžiosiomis raidėmis.")
#     elif tekstas.islower():
#         print("Tekstas parašytas mazom raidėmis.")
#     elif tekstas.istitle():
#         print("Tekstas parašytas is dideles raidės.")
#     else: print('tekstas misrus')   

# elif not tekstas.isalnum():
#     print("yra specialiu simboliu")


# skaicius = input('kiek pirksite zvakiu? ')
# kaina = 1

# skaicius = int(skaicius)
# if skaicius >= 1000 and skaicius < 2000:
#     print(f'mokesite už {skaicius} žvakių {(skaicius*kaina)-(skaicius * kaina*0.03)} eur')
# elif skaicius >= 2000:
#     print(f'mokesite už {skaicius} žvakių {(skaicius*kaina)-(skaicius * kaina*0.04)} eur')
# else: print(f'mokesite už {skaicius} žvakių {(skaicius*kaina)} eur')



# Paprašykite vartotojo įvesti tris skaičius. Suskaičiuokite įvesčių aritmetinį vidurkį. 
# Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10 arba didesnės nei 90.
#  Abu vidurkius atspausdinkite.


# skaicius1 = int(input('iveskite 1 skaiciu = '))
# skaicius2 = int(input('iveskite 2 skaiciu = '))
# skaicius3 = int(input('iveskite 3 skaiciu = '))
# bendras=0
# print(((skaicius1+skaicius2+skaicius3)/3))



# if skaicius1 <90 and skaicius1 > 10:
#     bendras+=1
# else: skaicius1 = 0
# if skaicius2 <90 and skaicius2 > 10:
#     bendras+=1
# else: skaicius2 = 0
# if skaicius3 <90 and skaicius3 > 10:
#     bendras+=1
# else: skaicius3 = 0

# if bendras != 0:
#     print(((skaicius1 + skaicius2 + skaicius3) / bendras))
# else:
#     print("Negalima dalinti iš nulio – nei vienas skaičius nepatenka į intervalą tarp 10 ir 90.")


# #Vartotojas įveda keturis skaičius, kurie privalo būti nuo 0 iki 2. Suskaičiuokite kiek yra įvesta nulių, vienetų ir dvejetų. 

# skaicius4 = int(input('iveskite 1 skaiciu = '))
# skaicius5 = int(input('iveskite 2 skaiciu = '))
# skaicius6 = int(input('iveskite 3 skaiciu = '))
# skaicius7 = int(input('iveskite 4 skaiciu = '))

# skaiciai = []
# netinkamiSkaiciai = []

# if skaicius4 >= 0 and skaicius4 <= 2:
#     skaiciai.append(skaicius4)
# else:
#     netinkamiSkaiciai.append(skaicius4)
# if skaicius5 >= 0 and skaicius5 <= 2:
#     skaiciai.append(skaicius5)
# else:
#     netinkamiSkaiciai.append(skaicius5)
# if skaicius6 >= 0 and skaicius6 <= 2:
#     skaiciai.append(skaicius6)
# else:
#     netinkamiSkaiciai.append(skaicius6)
# if skaicius7 >= 0 and skaicius7 <= 2:
#     skaiciai.append(skaicius7)
# else:
#     netinkamiSkaiciai.append(skaicius7)

# nuliu_skaicius = skaiciai.count(0)
# vienetu_skaicius = skaiciai.count(1)
# dvejetu_skaicius = skaiciai.count(2)

# print(f"Ivestyje yra {nuliu_skaicius} nulis(-iai), {vienetu_skaicius} vienetas(-ai), {dvejetu_skaicius} dvejetas(-ai).")
# print(f"netinkami ivesti skaiciai: {netinkamiSkaiciai}")

# Įvestis_1 = int(input("Įveskite skaičių:"))
# Įvestis_2 = int(input("Įveskite skaičių:"))
# Įvestis_3 = int(input("Įveskite skaičių:"))

# listas = [Įvestis_1, Įvestis_2, Įvestis_3]
# listas.sort()
# print(f"Visi skaičiai: {listas}, vidurinis skaičius yra {listas[1]}")


