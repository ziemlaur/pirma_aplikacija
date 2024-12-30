# def listas(l1):
#     l2 = [l1[0],l1[-1]]
#     print(l2)
    


# listas([1,2,56,98,78,85])
# import math

# def GT(greitis):
#     if greitis <= 50:
#         print('OK')
#     if greitis > 50:
#        taskai = (greitis - 50)/5
#        suapvalinta = math.floor(taskai)
#        print(suapvalinta)
#     if taskai >= 8:
#         print(f'taskai : {taskai}. atimtos teises')

# GT(92)


# def keicia(tekstas):
#     print((tekstas[-1] + tekstas[1:-1] + tekstas[0]))

# keicia('Labas rytas')
    

# def keiciaZodi(tekstas):
#     listas = list(tekstas)
#     naujas = []
#     for indexas in range(len(listas) -1, -1, -1):
#         naujas.append(listas[indexas])
#         reverse = ''.join(naujas)
#     print(reverse)


# keiciaZodi(' labas grazus pasauli')


# def atvirkscias_zodis(zodis):
#     return zodis[::-1]

# print(atvirkscias_zodis("Dangus"))


# def sekos(l1, l2):
                                    # 1 budas
    # s1 = set(l1)
    # s2 = set(l2)
    # inter = s1.intersection(s2)
    # print(inter)
    #                                 2 budas 
    # listas = []
    # for index, i in enumerate(l1):
    #     for index, j in enumerate(l2):
    #         if i == j:
    #             listas.append(j)
    # print(listas)

                                    # 3 budas
    # Rezult = []
    # for skaicius in l1:
    #     if skaicius in l2 and not skaicius in Rezult:
    #         Rezult.append(skaicius)
    # print(Rezult)

# sekos([1,2,3,4,5], [2,3,5,6])


def vidurkiai(raktazodis, *skaicius):

    if raktazodis == 'A':
        print(f"sekos aritmetinis vidurkis = {(sum(skaicius)/len(skaicius))}")
        sandauga = 1
        for skaitmuo in skaicius:
            sandauga *= skaitmuo
    
    
    if raktazodis == 'G':
        sandauga = 1
        for skaitmuo in skaicius:
            sandauga *= skaitmuo
        geometrinis_vidurkis = sandauga ** (1 / len(skaicius))
        print(f"sekos geometrinis vidurkis = {geometrinis_vidurkis}")

vidurkiai('A', 2, 4, 66)