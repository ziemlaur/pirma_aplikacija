import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="", 
    database ='zmones')

print('connected')
cur = cnx.cursor()


cur.execute('SELECT * FROM zmogus')
data = cur.fetchall()
print(data)

rezimas = input('N - new, E - Edit, D - delete, F - filter: ')

def pridejimas():
 
    vardas=input('vardas: ')
    pavarde=input('pavarde: ')
    metai=input('metai: ')

    cur.execute(f"INSERT INTO zmogus (Vardas, Pavarde, Metai) VALUES ('{vardas}', '{pavarde}', '{metai}')")
    cnx.commit()
    print("added info")

def redagavimas ():

    ID = input('ID: ')
    vardas=input('vardas: ')
    pavarde=input('pavarde: ')
    metai=input('metai: ')
    cur.execute(f"UPDATE zmogus SET Vardas = '{vardas}', Pavarde = '{pavarde}', Metai = '{metai}' WHERE ID = {ID} ")

    cnx.commit()
    print("updated info")

def istrynimas():

    ID = input('ID: ')
    cur.execute(f"SELECT Pavarde FROM zmogus WHERE ID = {ID}")
    data1 = cur.fetchone()
    if data1 and data1[0]== 'Ziemelyte':
        cur.execute(f"DELETE FROM zmogus WHERE ID = {ID}")
        cnx.commit() 
        print("info deleted")
    else: 
        print('info not deleted, no such ID or Pavarde is not Ziemelyte')

def filtras():
    cur.execute('SELECT ID, Metai FROM zmogus')  
    data = cur.fetchall()
    
    for i in data:
        ID, metai = i
        if '25' in str(metai): 
            cur.execute(f"UPDATE zmogus SET Metai = 69 WHERE ID = {ID}")
            cnx.commit()
            print(f"Updated Metai to 69 for ID {ID}")

    print("Filtering and updates completed.")



if rezimas.lower == 'n':
    pridejimas()
elif rezimas.lower == 'e':
    redagavimas()
elif rezimas.lower == 'd':
    istrynimas()
elif rezimas.lower == 'f':
    filtras()
else: 
    print('wrong input')
    
