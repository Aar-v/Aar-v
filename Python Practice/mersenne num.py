# function to print meserne number .
def mersennenum ( n ) :
    for a in range( 1 , n + 1 ) :
        mersnum = ( 2 ** a ) - 1
        print( mersnum , end = ' ' )
    print( )

#__main__.
n = int( input( " Enter no of required terms : " ) )
mersennenum( n )
       
