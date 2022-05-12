# String to capitalize first word in a string,
def Capitalstring ( String ) :
    n = len( S )
    a = 0
    end = n
    S2 = ' '
    while a < n :
        if a == 0 :
            S2 += S[ 0 ].upper( )
            a += 1
        elif S[ a ] == ' ' and S[ a + 1 ] != ' ' :
            S2 += S[ a ]
            S2 += S[ a + 1 ].upper( )
            a += 2
        else :
            S2 += S[ a ]
            a += 1
    print( " Orignal String : " , S )
    print( " Capitalized word string : " , S2 )

#__main__.
S = input( " Enter a string : " )
Capitalstring( S )
