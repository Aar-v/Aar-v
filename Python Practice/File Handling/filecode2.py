# Reading a file's first three lines - line by line .

myfile = open( r'C:\Users\Admin\Desktop\poem.txt', 'r' )
str1 = myfile.readline( )
print( str1 , end = ' ' )
str2 = myfile.readline( )
print( str2 , end = ' ' )
str3 = myfile.readline( )
print( str3 , end = ' ' )
myfile.close( )
