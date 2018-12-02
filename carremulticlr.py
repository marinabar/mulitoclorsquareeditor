from PIL import Image
img = Image.open("avantages-quil-y-a-a-grandir-dans-un-petit-village.jpg")
pixels = img.load()
for i in range(img.width//2, img.width ):
    for j in range(img.height//2, img.height):
        r, g, b = pixels[i, j]
        r+=39
        g+=90
        b+=18
        pixels[i, j]=(r, g, b)

for k in range(0, img.width//2):
    for t in range(0, img.height//2):
        r, g, b = pixels[k, t]
        g+=10
        r+= 25
        b+=130
        pixels[k, t]=(r, g, b)

for z in range(img.width//2,  img.width):
    for x in range(0, img.height//2):
        r, g, b = pixels[z, x]
        b+=130
        r+=10
        g+=190
        pixels[z, x]=(r, g, b)

for y in range(0,  img.width//2):
    for f in range(img.height//2, img.height):
        r, g, b = pixels[y, f]
        b+=45
        r+=150
        g+=5
        pixels[y, f]=(r, g, b)  

img.show()
        
        
    
