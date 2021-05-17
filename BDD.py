import pymysql
import Create_BDD

# table creation if not exist
Create_BDD.Create_table()

# database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="b2_proj_dev_log" )
cursor = connection.cursor()

# database close
connection.close()