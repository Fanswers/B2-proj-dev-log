import pymysql

def Create_table():
    # Database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="b2_proj_dev_log" )
    cursor = connection.cursor()

    # Query for creating table
    JoueurTableSql = """CREATE TABLE IF NOT EXISTS Joueur(
    ID INT(20) PRIMARY KEY AUTO_INCREMENT,
    NAME  CHAR(20) NOT NULL,
    PASSWORD CHAR(20) NOT NULL,
    LEVEL INT(20) NOT NULL,
    WIN INT(20) NOT NULL,
    LOOSE INT(20) NOT NULL)"""

    cursor.execute(JoueurTableSql)

    # Close database connection
    connection.close()

def Connection(log):
    # Database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="b2_proj_dev_log")
    cursor = connection.cursor()

    # Loop function connection
    ConnectionUser = False
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
            log = test
        else:
            print("Nom de compte ou mot de passe incorrecte.")

    # Close database connection
    connection.close()

    # Return information of the account
    if ConnectionUser:
        print("Tu es connecté !")
        return log

