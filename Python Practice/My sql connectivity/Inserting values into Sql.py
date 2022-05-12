# Inserting values in table.

import mysql.connector as sqltor
mycon = sqltor.connect( host = 'localhost' , user = 'root' , password = 'abhi@132' , database = 'test' )
if mycon.is_connected( ) == False :
    print( " Error connecting to mysql database " )
cursor = mycon.cursor( )
st = " Insert into student( rollno , name , marks , grade , section ) values( 108 , 'Eka' , 84.0 , 'A' , 'B' ) " 
cursor.execute( st )
mycon.commit( )




