# matplotlib code 4 .
import matplotlib.pyplot as plt
import numpy as np
val = [ [ 5 , 25 , 45 , 20 ] , [ 4 , 23 , 49 , 17, ] , [ 6 , 22 , 47 , 19 ] ]
x = np.arange( 4 )
plt.bar( x + 0.00 , val[ 0 ] , color = 'b' , width = 0.25 , label = 'Range 1 ' )
plt.bar( x + 0.25 , val[ 1 ] , color = 'g' , width = 0.25 , label = 'Range 2 ' )
plt.bar( x + 0.50 , val[ 2 ] , color = 'r' , width = 0.25 , label = 'Range 3 ' )
plt.title( " Multirange barchart " )
plt.xlabel( " X " )
plt.ylabel( " Y " )
plt.legend( loc = ' upper right ' )
plt.show( )
