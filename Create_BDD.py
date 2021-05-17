import pymysql

def Create_table():
    #database connection
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

    # some other statements  with the help of cursor
    cursor.execute(JoueurTableSql)
    connection.close()