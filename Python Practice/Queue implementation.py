# Python program to implement QUEUE OPERATIONS .

" " "   Queue : Implemented as list.  " " "
" " "   Front : Integer having position of first ( Foremost ) element in queue . " " "
" " "   Rear : Integer having position of last element in queue . " " "

def Cls( ) :
    print( " \n " * 100 )

def isEmpty( qu ) :
    if qu == [ ] :
        return True
    else :
        return False

def Enqueue ( qu ,  item ) :
    qu.append( item )
    if len( qu ) == 1 :
        front = rear = 0
    else :
        front = 0
        rear = len( qu ) - 1

def Dequeue ( qu ) :
    if isEmpty( qu ):
        return " Underflow "
    else :
        item = qu.pop( 0 )
    if len( qu ) == 0 :
        front = rear = None
    return item

def Peek ( qu ) :
    if isEmpty( qu ) :
        return " Underflow "
    else :
        front = 0
        return qu[ front ]

def Display ( qu ) :
    if isEmpty ( qu ) :
        print( " Queue is empty !!! " )
    elif len( qu ) == 1 :
        print( qu[ 0 ] , " \t < == front " )
    else :
        front == 0
        rear = len( qu ) - 1
        print( qu[ 0 ] , " \t < -- front " )
        for a in range( 1 , rear ) :
            print( qu[ a ] )
        print( qu[ rear ] , " < \t < -- rear " )

#__main__.
Queue = [ ]
front = rear = None

while True :
    Cls( )
    print( " QUEUE OPERATIONS !!! " )
    print( " Choose your option from the following : ")
    print( " 1. Enqueue " )
    print( " 2. Dequeue " )
    print( " 3. Peek ")
    print( " 4. Display Queue " )
    print( " 5. Exit " )

    ch = int( input( " Enter your choice : " ) )

    if ch == 1 :
        item = int( input( " Enter item : " ) )
        Enqueue( Queue , item )
        input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )

    elif ch == 2 :
        item = Dequeue( Queue )
        if item == " Underflow " :
            print ( " Underflow ! Queue is empty ! " )
        else :
            print( " Dequeue-ed item is " , item )
            input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " ) 

    elif ch == 3 :
        item = Peek( Queue )
        if item == " Underflow " :
            print( " Underflow ! Queue is empty ! " )
        else :
            print( " Frontmost item is " , item )
            input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )

    elif ch == 4 :
        Display( Queue )
        input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )
    elif ch == 5 :
        print( " Are you sure you want to exit. " )
        aaa =int( input( " Press 1 to go bact to menu , Press 2 to Exit : " ) )
        if aaa == 1 :
            input( " Press enter to return to menu .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )
        elif aaa == 2 :
            print( " OK !!!, Exiting the Menu " )
            break
        else :
            print( " Invalid choice " )
            input( " Press enter to return to menu .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )

    else :
        print( " Invalid Choice !!! " )
        input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )
        
        

        


