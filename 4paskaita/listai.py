sarasas = [
    'Asta',
    'Tomas',
    'Mynde',
    'Tomas',
    1634
]

print (sarasas)

# pirmos reiksmes spausdinimas

print(sarasas[0])

sarasas.append(123)
print(sarasas)

sarasas.insert(2, 'Laura')
print(sarasas)

sarasas.pop(5)
print(sarasas)

print(sarasas.count('Laura'))

sarasas.clear()
print(sarasas)

sarasas = ['A','B','C','D','E','F','G']

print (sarasas[2:5])
#kas penkta ir kas antra
print (sarasas[::5])
print (sarasas[::2])

#konvertuoti str i list. isskaidom pagal tarpelius.
tekstas = 'ka as zinau ka cia daugiau pasakyti'
#print(tekstas.split(.))   -  jeigu skaidytume pagal taskus

print(tekstas.split())

zodziai = tekstas.split()
print(zodziai[0])

print(' '.join(zodziai))





#SAVARANKISKAS DARBAS
#1
pirmas = int(input('1 sk'))
antras = int(input('2 sk'))
trecias = int(input('3 sk'))
ketvirtas = int(input('4 sk'))
penktas = int(input('5 sk'))

sum = ((pirmas+antras+trecias+ketvirtas+penktas)/5)
print('vidurkis: '+str(sum))

#2

metrai = int(input('iveskite skaiciu metrais'))

print('centi: ' +str(metrai*100) + ' mili: ' +str(metrai*1000) + ' km: ' +str(metrai/1000))


#3
pirmasS = int(input('iveskite 1 sk: '))
antrasS = int(input('iveskite 2 sk: '))

liekana = (pirmasS % antrasS)
print(liekana)

#4

pirmasSk = int(input('iveskite 1 sk: '))
antrasSk = int(input('iveskite 2 sk: '))

pakelimas = pirmasSk ** antrasSk
print(pakelimas)

#5

lst = ['Python', 'yra', 'lengva', 'programavimo', 'kalba']

print(lst[0],lst[-1])
print(lst[::2])
print(type(lst[-2]))
print(type(lst[0]), len(lst[0]))

#6

txt = ' Aš rytais mėgstu kavą su sumuštiniais ir arbatą su pyragu'
print(len(txt.split()),txt.split()[::2])
# 7


l = ['Vilnius', 1323, ['Nupirkti maisto', 'PABegioti'], 8, 'rytas']
print(l[1], l[0].upper())

print(l[2][0][-3:].upper())


l = ['Vilnius', 1323, ['Nupirkti maisto','PABegioti'], 8, 'rytas']
print(l[1], l[0].upper())

print(l[2][0][-3:].upper())


print((l[2][1][0:3]).isupper())

