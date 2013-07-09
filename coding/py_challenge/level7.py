import Image

im = Image.open("../images/oxygen.png")
print "Image info:",im.format, im.size, im.mode

height = 0
for h in range(im.size[1]):
    pixel = im.getpixel((0, h))
    if(pixel[0]==pixel[1] and pixel[1]==pixel[2]):
        height = h
        break

ascii = [-1]
for w in range(0, im.size[0], 7):
    pixel = im.getpixel((w, height))
    if(pixel[0]==pixel[1] and pixel[1]==pixel[2]):
        ascii.append(pixel[0])
    else:
        break

ascii.remove(-1)
print "".join([chr(asc) for asc in ascii])