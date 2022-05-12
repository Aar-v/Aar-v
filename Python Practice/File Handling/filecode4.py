# Program to display no of lines in a file.

myfile = open( r'C:\Users\Admin\Desktop\poem.txt', 'r' )
s = myfile.readlines( )
linecount  = len( s )
print( " Number of lines in poem.txt is " , linecount )
myfile.close( )
