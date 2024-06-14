from mysql.connector import connect
import app.settings as settings

mydb = connect(host=settings.MYSQL_HOST,user=settings.MYSQL_USER,password=settings.MYSQL_PASSWORD,database=settings.MYSQL_DATABASE,port=settings.MYSQL_PORT)
mycursor = mydb.cursor(buffered=True)

