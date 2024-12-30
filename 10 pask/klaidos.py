

#                                               su ifu,
while True:
    try:
        skaiciusA = int(input('Pirmas skaičius: '))
        skaiciusB = int(input('Antras skaičius: '))
        veiksmas = input('Įveskite matematinio veiksmo simbolį (+, /, *, -): ')

        if veiksmas == '/':
            if skaiciusB == 0:
                print('Dalyba iš nulio negalima, įveskite kitą skaičių.')
                continue
            rezultatas = skaiciusA / skaiciusB
        elif veiksmas == '+':
            rezultatas = skaiciusA + skaiciusB
        elif veiksmas == '-':
            rezultatas = skaiciusA - skaiciusB
        elif veiksmas == '*':
            rezultatas = skaiciusA * skaiciusB
        else:
            print('Neteisingas veiksmas, įveskite +, -, * arba /.')
            continue

        print(f'Rezultatas: {rezultatas}')
        break  

    except ValueError:
        print('ivesta raidine reikšme, įveskite skaičių.')


        
                                                # du exceptionai 

# while True:
#     try:
#         skaiciusA = int(input('Pirmas skaičius: '))
#         skaiciusB = int(input('Antras skaičius: ')) 
        
#         dalyba = skaiciusA / skaiciusB 
#         suma = skaiciusA + skaiciusB
#         atimtis = skaiciusA - skaiciusB
#         daugyba = skaiciusA * skaiciusB
        
#         print(f'Dalyba: {dalyba}, Suma: {suma}, Atimtis: {atimtis}, Daugyba: {skaiciusA * skaiciusB}')
#         break

#     except ZeroDivisionError:
#         print('Dalyba iš nulio negalima.')
#     except ValueError:
#         print('Įvesta raide, įveskite skaičių.')

