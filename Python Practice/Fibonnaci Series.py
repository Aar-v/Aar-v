# Fibonnaci Series .
def fibonacciSeries( n ) :
    first = 0
    second = 1
    print( first , end = ' , ' )
    print( second , end = ' , ' )
    for i in range ( 1 , n ) :
        third = first + second
        print( third , end = ' , ' )
        first, second = second, third
    print(". . . . . . . . . . . . . . . . " )

#__main__.
n = int( input ( " Enter no of items in series : " ) )
print(". . . . . . . . . . . . . . . . " )
fibonacciSeries( n )

