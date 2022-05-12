# matplotlib code 3.
import matplotlib.pyplot as plt
import numpy as np
cities, population = [ 'Delhi' , 'Mumbai' , 'Banglore' , 'Hyderabad' ] , [ 23456123 , 20083104 , 18456123 , 13411093 ]
plt.barh( cities , population )
plt.ylabel( ' Cities ' )
plt.xlabel( ' Population ' )
plt.show( )
