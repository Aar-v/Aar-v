# tkinter code.

import tkinter

def wquit( ) :
    print( " Hello , getting out of here " )

root = tkinter.TK( )
widgt1 = tkinter.Label( root , text = " Hello there " )
widgt1.pack(  )
widgt2 = tkinter.Button( root , text = " Click to quit " )
widgt2.pack( )
root.mainloop( )
