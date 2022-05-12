# Linear search.

def Lsearch( AR , ITEM ) :
    i = 0
    while i < len( AR ) and AR[ i ] != ITEM :
        i += 1
    if i < len( AR ) :
        return i
    else:
        return False

N = int( input( " Enter deired linear list size( max : 50 ) . . . : " ) )
print( " \n Enter elements for linear list \n " )
AR = [ 0 ] * N
for i in range( N ) :
    AR[ i ] = int( input( " Element " + str( i ) + " : "  ) )

ITEM = int( input( " \n Enter element to be searched for : " ) )
index = Lsearch( AR , ITEM )

if index :
    print( " \n Element found at index : " , index , " \n Position : " , ( index + 1 ) )
else  :
    print( " \n Sorry !! Given element could not be found. \n " ) 
