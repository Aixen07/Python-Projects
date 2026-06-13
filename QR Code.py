import qrcode

url = input("Enter your URL: ")
filename = input("Enter File Name You Want to Save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"
img = qrcode.make(url)
type(img)  
img.save(filename)
