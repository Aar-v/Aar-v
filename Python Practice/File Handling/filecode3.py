# Program to display the size of a file after removing EOL characters , leading and trailing white spaces and blank
# lines.

myfile = open( r'C:\Users\Admin\Desktop\poem.txt', 'r' )
str1 = ' '
size = tsize = 0
while str1 :
    str1 = myfile.readline( )
    tsize = tsize + len( str1 )
    size = size + len( str1.strip( ) )
print( " Size of the file after removing all EOL characters & blank lines : " ,  size)
print( " Total size of the file  : ", tsize )
myfile.close( )
