#import Lib
#install 
#pip install beautifulsoup4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import base64
import tkinter as tk 



#input of User
print("Please MaKe Suer You are Connected to Internet")

print("Enter the Input Ex:-10101 ")
x = str(input())
imageFinal = ''
l =  []
#connecting to url
url = 'http://www.ee.unb.ca/cgi-bin/tervo/encoding.pl?binary='+x
#scrapping webPage
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.gif')})
for image in images: 
   l.append(image['src'])

#Collecting the useful result
for i in range(len(l)):
    if 'trellis' in l[i]:
        imageFinal = l[i]
        
#processing the image        
q = imageFinal.split('?')  
q.insert(1, '/')
q.insert(2, '?')
imageFinal = ''.join(q)

#our Final Url
getUrLImage = 'http://www.ee.unb.ca/cgi-bin/tervo/'+imageFinal

#making ui using tkinter
root = tk.Tk()
w = 800
h = 500
x = 1
y = 100
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
image_byt = urlopen(getUrLImage).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)

#creating a White Background
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(10, 10, image=photo, anchor='nw')
root.mainloop()



