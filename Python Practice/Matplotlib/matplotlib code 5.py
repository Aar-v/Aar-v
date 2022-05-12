# matplotlib code 5.
import numpy as np
import matplotlib.pyplot as plt
contri = [ 17 , 8.8 , 12.75 , 14 , 0.1 ]
houses = [ ' Vidya ' , ' Kasma ' , ' Namrata ' , ' Karuna ' , ' New ' ]
plt.pie( contri , labels = houses , autopct = '%2.2f%%' )
plt.show
