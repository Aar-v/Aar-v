# To check wether a string is pallindrome or not.
def pallindrome ( string ) :
    n = len( S )
    mid = int(n/2)
    rev = -1
    for a in range ( mid ) :
        if S[ a ] == S[ rev ] :
            a += 1
            rev -= 1
        else :
            print( S, "  is not pallindrome " )
            break
    else :
        print( S , " is pallindrome " )

#__main__.
S = input( " Enter a string : " )
pallindrome( S )
input( ' Press enter to close ' )
