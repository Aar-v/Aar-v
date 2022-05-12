# matplotlib code 2
import matplotlib.pyplot as plt
import numpy as np
a = np.arrange( 1 , 20 , 1.25 )
b = np.log(a)
plt.plot( a, b )
plt.xlabel( " Random Values " )
plt.ylabel( " Lograthmic Values " )
c = np.cos( a )
plt.plot(a , c 'bo' , linestyle = " dashdot " )
plt.show( )








