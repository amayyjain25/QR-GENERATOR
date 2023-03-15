import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1
                   ,error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=5,)
n = str(input("Enter the link"))
qr.add_data(n)
qr.make(fit=True)
c1= str(input("enter colour of your qr"))
c2= str(input("enter background colour"))
img =qr.make_image(fill_color=c1 ,back_color=c2)
name= str(input("enter name with .png in end"))
img.save(name)
#img = qr.make("www.linkedin.com/in/amayyjain")
#img.save("LINKEDIN QR.png")

