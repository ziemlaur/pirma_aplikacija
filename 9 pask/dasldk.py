simbolis = (input('ivesk sim: '))
kiekis = int(input(' kiekis : '))

for i in range(kiekis):
    if i == 0 or i == kiekis - 1:
        print(simbolis *kiekis)
    else:
        print(simbolis + ' ' * (kiekis - 2) + simbolis)