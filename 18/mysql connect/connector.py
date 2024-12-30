import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="", 
    database ='zmones')

print('connected')
cur = cnx.cursor()

# cur.execute('SELECT * FROM country_data')
# data = cur.fetchall()

# pirmas = int(input('pajamos :'))
# antras = int(input('gdpp :'))
# print(pirmas, antras)
# cur.execute(f'SELECT country_name FROM country_data WHERE income > {pirmas} AND gdpp < {antras}')
# data = cur.fetchall()

# print(data)

# raide = input('raide: ')
# cur.execute(f"SELECT inflation FROM country_data WHERE country_name LIKE '%{raide}%'")
# data1 = cur.fetchall()

# print(data1)

# raide = input('raide: ')
# amzius = int(input('amzius: '))
# cur.execute(f"SELECT inflation FROM country_data WHERE country_name LIKE '%{raide}%' AND life_expectancy < {amzius}")
# data2 = cur.fetchall()

# print(data2)

# pavadinimas=input('pav.:')
# aprasymas=input('apr.:')
# zanras=input('zanras:')

# cur.execute(f"INSERT INTO filmas (pavadinimas, aprasymas, zanras) VALUES ('{pavadinimas}', '{aprasymas}', '{zanras}')")
# cnx.commit()
# print("added info")

# cnx.close()


# def pridejimas():
 
#     vardas=input('vardas:')
#     pavarde=input('pavarde:')
#     metai=input('metai:')

#     cur.execute(f"INSERT INTO zmogus (Vardas, Pavarde, Metai) VALUES ('{vardas}', '{pavarde}', '{metai}')")
#     cnx.commit()
#     print("added info")

# def spausdinimas():
#     cur.execute('SELECT * FROM zmogus')
#     data = cur.fetchall()
#     print(data)


# rezimas = input('iveskite p jeigu norite prideti zmogu, iveskite betkokia kita raide jeigu norite pamatyti visa lentele: ')

# if rezimas == 'p':
#     pridejimas()
# else:
#     spausdinimas()


# cnx.close()



# cur.execute(f"UPDATE zmogus SET Vardas = 'Laura', Pavarde = 'Ziemelyte' WHERE ID = 3")
# cnx.commit()
# print("info updated")

cur.execute(f"DELETE FROM zmogus WHERE ID = 4")
cnx.commit()
print("info deleted")
