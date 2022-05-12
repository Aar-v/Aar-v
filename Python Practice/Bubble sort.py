# Bubble Sort.
def bubblesort ( List ) :
    n = len( A )
    for i in range( n ) :
        for j in range( 0 , n-i-1 ) :
            if A[ j ] > A [  j + 1 ] :
                A[ j ], A [  j + 1 ] = A[  j +1 ], A[ j ]
    print ( " List after sorting : " , A )
#__main__.
A = eval( input ( " Enter a list : " ) )
print( " The orignal list is : " , A )
bubblesort( A )
          
             
