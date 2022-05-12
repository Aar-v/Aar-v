# Binary search iterative program.

def bsearch ( ar , key ) :
    low = 0
    high = len( ar ) -1
    while low <= high :
        mid = int( ( low + high ) / 2 )
        if key == ar[ mid ] :
            return mid
        elif key < ar[ mid ] :
            high = mid - 1
        else :
            low = mid + 1
    else :
        return -999

#__main__.
ar = eval( input ( " Enter a list ' { in [ ] } ' : " ) )
item = int( input( " Enter search item : " ) )
res = bsearch( ar , item )
if res >= 0 :
    print( item , " FOUND !!! , at index : " , res )
else :
    print( " SORRY !!!!! ,  " , item , " not found in array " )

