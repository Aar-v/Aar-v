# Program that displays first three rows fetched from student table of MySQL database and close the connection.

import mysql.connector as sqltor
mycon = sqltor.connect( host = 'localhost' , user = 'root' , password = 'abhi@132' , database = 'test' )
if mycon.is_connected( ) == False :
    print( " Error connecting to mysql database " )
cursor = mycon.cursor( )
cursor.execute( " select * from student " )
data = cursor.fetchmany( 3 )
for row in data :
    print( row )
mycon.close( )

