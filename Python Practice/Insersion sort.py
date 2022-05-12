# Insersion Sort.
def insersionsort ( List ) :
    n = len( A )
    for i in range ( 1 , n ) :
        key = A[ i ]
        j = i - 1
        while j >= 0 and key < A[ j ] :
            A[ j + 1 ] = A[ j ]
            j -= 1
        else :
            A[ j + 1 ] = key
    print( " The list after sorting is : " , A )

#__main__.
A = eval( input( "Enter a list : " ) )
print( " The orignal list is : " , A )
insersionsort( A )

          
