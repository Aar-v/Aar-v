# Python program to implement STACK OPERATIONS .

" " "   Stack : Implemented as list  " " "
" " " top : Integer having position of topmost element in Stack. " " "

def Cls( ) :
    print( " \n " * 100 )

def isEmpty( stk ) :
    if stk == [ ] :
        return True
    else :
        return False

def Push( stk , item ) :
    stk.append( item )
    top = len( stk ) - 1

def Pop ( stk ) :
    if isEmpty( stk ) :
        return " Underflow "
    else :
        item = stk.pop( len(stk) - 1 )
        if len( stk ) == 0 :
            top = None
        else :
            top = len( stk ) -1
        return item

def Peek ( stk ) :
    if isEmpty( stk ) :
        return " Underflow "
    else :
        top = len( stk ) - 1
        return stk[ top ]

def Display ( stk ) :
    if isEmpty( stk ) :
        print( " Stack is Empty !!! " )
    else :
        top = len( stk ) - 1
        print( stk[ top ] , " \ t  <- Top " )
        for a in range( top -1 , -1 , -1 ) :
            print( stk[ a ] )

#__main__.
Stack = [ ]
top = None

while True :
    Cls( )
    print( " STACK OPERATIONS !!! " )
    print( " Choose your option from the following : ")
    print( " 1. Push " )
    print( " 2. Pop " )
    print( " 3. Peek ")
    print( " 4. Display Stack " )
    print( " 5. Exit " )

    ch = int( input( " Enter your choice : " ) )

    if ch == 1 :
        item = int( input( " Enter item : " ) )
        Push( Stack , item )
        input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )

    elif ch == 2 :
        item = Pop( Stack )
        if item == " Underflow " :
            print( " Underflow !! , Stack is empty . " )
        else :
            print( " Popped item is : " , item )
        input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )

    elif ch == 3 :
        item = Peek( Stack )
        if item == " Underflow " :
            print( " Underflow !! , Stack is empty . " )
        else :
            print( " Topmost item is : " , item )
        input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )

    elif ch == 4 :
        Display( Stack )
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
        print( " Invalid choice " )
        input( " Press enter to continue .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. " )
        
    
            
