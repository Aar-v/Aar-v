# Recursive program to print factorial .
def factorial ( n ) :
    if n < 2 :
        return 1
    return n * factorial( n - 1 )

#__main__
n = int( input( " Enter no of required terms ( > 0 ) : " ) )
print( " The factorial of " , n , " terms is : " , factorial( n ) )
