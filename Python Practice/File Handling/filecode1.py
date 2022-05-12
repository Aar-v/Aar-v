# Code to read n bytes and then read mmore bytes from the last position read.

myfile = open( r'C:\Users\Admin\Desktop\poem.txt', 'r' )
str1 = myfile.read( 30 )
print( str1 )
str2 = myfile.read( 50 )
print( str2 )
myfile.close( )
