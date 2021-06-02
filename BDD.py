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

def Connection(login, password):
    # Database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="b2_proj_dev_log")
    cursor = connection.cursor()

    # Loop function connection
    ConnectionUser = False
    while not ConnectionUser:
        ndc = login
        cursor.execute("Select * from Joueur where Name = %s", ndc)
        test = "0"
        for row in cursor:
            test = row
        if len(test) != 6:
            return False
        mdp = password
        if test[2] == mdp:
            ConnectionUser = True
            log = test
        else:
            return False

    # Close database connection
    connection.close()

    # Return information of the account
    if ConnectionUser:
        return True
