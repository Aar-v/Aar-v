# Fetchmany( ) method.

import mysql.connector as sqltor
mycon = sqltor.connect( host = 'localhost' , user = 'root' , password = 'abhi@132' , database = 'test' )
if mycon.is_connected( ) == False :
    print( " Error connecting to mysql database " )
cursor = mycon.cursor( )
cursor.execute( " select * from student " )
data = cursor.fetchmany( 4 )
count = cursor.rowcount
print( " Total no of rows recieved in the result : " , count )
for row in data :
    print( row )

