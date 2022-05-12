# Binary Search recursive program .
def bsearch ( ar , key , low , high ) :
    if low > high :
        return -999
    mid = int ( ( low + high ) / 2 )
    if key == ar[ mid ] :
        return mid
    elif key < ar [ mid ] :
        high = mid -1
        return bsearch( ar , key , low , high )
    else :
        low = mid + 1
        return bsearch( ar , key , low , high )

#__main__.
ar = eval( input ( " Enter a list ' { in [ ] } ' : " ) )
item = int( input ( " Enter Search item : " ) )
res = bsearch( ar , item , 0 , ( len( ar ) -1 ) )
if res >= 0 :
    print( item , " FOUND !!! , at index : " , res )
else :
    print( " SORRY !!!!!! " , item , " is not found in array " )
