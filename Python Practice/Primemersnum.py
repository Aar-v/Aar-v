# Function to print prime mersenne numbers.
def Primemersnum ( n ) :
    lst1 = [ ]
    lst2 = [ ]
    for a in range ( 1 , n + 1 ) :
        mersnum = ( 2 ** a ) - 1
        mid = int( mersnum/2 ) + 1
        lst1.append( mersnum )
        lst2.append( mid )
    g = len( lst1 )
    h = len( lst2 )
    for b in range ( h ) :
        for c in range( g ) :
            if lst1[ c ] % lst2[ b ] == 0 :
                print( mersnum )
            else :
                print( mersnum , " \t Prime " )

#__main__.
n = int( input( " Enter no of required terms : " ) )
Primemersnum( n )
         
