# class Objektas():
#     def __init__(self):
#         print('Objektas yra sukurtas')

# Objektas()


# class KonstDest():
#     def __init__(self):
#         print('Objektas yra sukurtas')

#     def __del__(self):
#         print('Objektas sunaikintas')

# KonstDest()
# del KonstDest


# class Vienas():
#     def __init__(self, vardas):
#         self.vardas = vardas 


# vienas = Vienas("Pradinis vardas")
# print(vienas.vardas)
# vienas.vardas = "Naujas vardas"
# print(vienas.vardas)




# class Vienas():
#     def __init__(self, vardas):
#         self.vardas = vardas 

#     def isvesti(self):
#         print(self.vardas)
    
#     def naujas(self, naujasVardas):
#         self.vardas = naujasVardas
#         print(self.vardas)
    
# vienas = Vienas('Senas vardas')
# vienas.isvesti()
# vienas.naujas('Naujas vardas')

                            #  televizorius


# class Televizorius():
#     def __init__(self, gamintojas):
#         self.gamintojas = gamintojas
#         self.kanalas = 1
#         self.garsas = 50
    
#     def padidinti_garsa(self, garsas):
#         if garsas < 100 and garsas > 0:
#             self.garsas = garsas
#         else:
#             self.garsas = 100
    
#     def sumazinti_garsa(self, garsas):
#         if garsas > 0 :
#             self.garsas = garsas
#         else:
#             self.garsas = 0
    
#     def keisti_kanala(self, naujas_kanalas):
#         if 1 <= naujas_kanalas <= 50:
#             self.kanalas = naujas_kanalas
#         else:
#             self.kanalas = 1  
    
#     def atstatyti_gamyklinius_parametrus(self):
#         self.kanalas = 1
#         self.garsas = 50
    
#     def __str__(self):
#         return f"Televizorius '{self.gamintojas}' šiuo metu rodo {self.kanalas} kanalą. Garso lygis {self.garsas}."


# tv = Televizorius("Sony")
# tv.keisti_kanala(8)
# tv.padidinti_garsa(76)
# tv.sumazinti_garsa()
# tv.atstatyti_gamyklinius_parametrus()
# print(tv) 


# class Mokinys:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pazymiai = []

#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)

#     def skaiciuoti_vidurki(self):
#         return sum(self.pazymiai) / len(self.pazymiai)

#     def didziausias_pazymys(self):
#         return max(self.pazymiai)

#     def maziausias_pazymys(self):
#         return min(self.pazymiai)
        
    
    


# class Abiturientas(Mokinys):
#     def __init__(self, vardas, pavarde):
#         super().__init__(vardas, pavarde)
#         self.egzaminai = []

#     def prideti_egzamino_rezultata(self, rezultatas):
#         self.egzaminai.append(rezultatas)

#     def skaiciuoti_bendra_vidurki(self):
#         visi_pazymiai = self.pazymiai + self.egzaminai
#         return sum(visi_pazymiai) / len(visi_pazymiai)


# class Mokykla:
#     def __init__(self):
#         self.mokiniai = []

#     def prideti_mokini(self, mokinys):
#         self.mokiniai.append(mokinys)

#     def pasalinti_mokini(self, vardas, pavarde):
#         naujas_sarasas = []
#         for m in self.mokiniai:
#             if m.vardas != vardas or m.pavarde != pavarde:
#                 naujas_sarasas.append(m)
#         self.mokiniai = naujas_sarasas

#     def skaiciuoti_visos_mokyklos_vidurki(self):
#         visi_pazymiai = []
#         for m in self.mokiniai:
#             print(m.vardas, "Mokinio vidurkis:", m.skaiciuoti_vidurki())
#             for p in m.pazymiai:
#                 visi_pazymiai.append(p)
        
     
#         print("Mokyklos vidurkis:", sum(visi_pazymiai) / len(visi_pazymiai))
    



# mokinys1 = Mokinys("Jonas", "Jonaitis")
# mokinys1.prideti_pazymi(8)
# mokinys1.prideti_pazymi(9)
# mokinys1.prideti_pazymi(10)
# mokinys2 = Mokinys('Zilvinas', 'Kapotinis')
# mokinys2.prideti_pazymi(7)
# mokinys2.prideti_pazymi(3)
# mokinys2.prideti_pazymi(5)
# mokinys3 = Mokinys('Agne', 'Petrikaite')
# mokinys3.prideti_pazymi(5)
# mokinys3.prideti_pazymi(6)


# abiturientas1 = Abiturientas("Petras", "Petraitis")
# abiturientas1.prideti_pazymi(7)
# abiturientas1.prideti_pazymi(9)
# abiturientas1.prideti_egzamino_rezultata(8)
# abiturientas1.prideti_egzamino_rezultata(10)

# mokykla = Mokykla()
# mokykla.prideti_mokini(mokinys1)
# mokykla.prideti_mokini(mokinys2)
# mokykla.prideti_mokini(mokinys3)
# mokykla.prideti_mokini(abiturientas1)

# mokykla.skaiciuoti_visos_mokyklos_vidurki()




# class Mokinys:
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pazymiai = []

#     def prideti_pazymi(self, pazymys):
#         if 0 <= pazymys <= 10:
#             self.pazymiai.append(pazymys)
#         else:
#             raise ValueError("Pažymys turi būti tarp 0 ir 10.")

#     def gauti_pazymius(self):
#         return self.pazymiai

#     def skaiciuoti_vidurki(self):
#         return sum(self.pazymiai) / len(self.pazymiai)

#     def didziausias_pazymys(self):
#         return max(self.pazymiai)

#     def maziausias_pazymys(self):
#         return min(self.pazymiai)


# import random

# class Vaisius:
#     def __init__(self):
#         self.dydis = random.randint(5, 25) 
#         self.id = random.randint(1000000, 9999999) 
#         self.prakastas = False  

#     def prakasti(self):
#         self.prakastas = True  
    
#     def __repr__(self):
#         return f"Vaisius(id={self.id}, dydis={self.dydis})"


# class Krepsys:
#     def __init__(self):
#         self.vaisiai = []  

#     def pripildyti(self):
#         while len(self.vaisiai) < 20:
#             vaisius = Vaisius()
#             self.vaisiai.append(vaisius)
#         self.vaisiai.sort(key=lambda vaisius: vaisius.dydis, reverse=True)

#     def isimti(self):
#         if self.vaisiai:
#             vaisius = self.vaisiai.pop(0)  
#             vaisius.prakasti() 
#             return vaisius
#         return None


# grauztukai = {}

# krepsys = Krepsys()
# krepsys.pripildyti()  

# for i in range(5):
#     vaisius = krepsys.isimti()  
#     if vaisius:
#         grauztukai[vaisius.id] = vaisius  

# print("Graužtukai:", grauztukai)

# krepsys.pripildyti()  
# print("\nKrepšys po papildymo:", krepsys.vaisiai)
# print("\nGraužtukai po papildymo:", grauztukai)

