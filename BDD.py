import pymysql
import Create_BDD

# table creation if not exist
Create_BDD.Create_table()

# database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="b2_proj_dev_log" )
cursor = connection.cursor()

ConnectionUser = False

a = 0
while not ConnectionUser:
    print("Nom de compte :")
    ndc = input()
    cursor.execute("Select * from Joueur where Name = %s", ndc)
    test = "0"
    for row in cursor:
        test = row
    print(test)
    print("Mot de passe :")
    mdp = input()
    cursor.execute("Select * from Joueur where Password = %s", mdp)
    test2 = "1"
    for row in cursor:
        test2 = row
    print(test2)
    if test == test2:
        ConnectionUser = True
    else:
        print("Nom de compte ou mot de passe incorrecte.")

if ConnectionUser:
    print("Tu es connecté !")

# database close
connection.close()