# function to print string in reverse order.
def revstr ( String ) :
    print( " The string : " , S , " in reverse order is : " , end = ' ' )
    n = len( S )
    for a in range ( -1 , -n-1 , -1 ) :
        print( S[ a ] , end = '' )

#__main__.
S = input( " Enter a string : " )
revstr( S )
