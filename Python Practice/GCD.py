# Gratest common divisor

def gcd ( p , q ) :
    if q == 0 :
        return p
    return gcd ( q , p % q )

#__main__.
n1 = int( input( " Enter first number : " ) )
n2 = int( input( " Enter second number : " ) )
d = gcd( n1 , n2 )
print ( " GCD of " , n1 , " and " , n2 , " is : " , d )
