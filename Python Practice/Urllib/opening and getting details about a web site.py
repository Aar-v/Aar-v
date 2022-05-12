# Urllib program.

import urllib
import webbrowser
weburl = urllib.request.urlopen( ' http://www.ted.com/ ' )
html = weburl.read( )
data = weburl.getcode( )
url = weburl.geturl( )
hd = weburl.headers
inf = weburl.info( )
print( " The URL is " , url )
print( " HTTP status code is : " , data )
print( " Headers returned \n " , hd )
print( " The info( ) returned : \n" , inf )
print( " Now opening the url " , url )
webbrouser.open_new( url )
