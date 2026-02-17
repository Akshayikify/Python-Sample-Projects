import qrcode
from qrcode.constants import ERROR_CORRECT_L

url=input("Enter the url: ")
trimmed_url=url.strip()
qr = qrcode.QRCode(
    version=1, 
    error_correction=ERROR_CORRECT_L, 
    box_size=10, 
    border=4, 
) 

qr.add_data(trimmed_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("advanced_qrcode.png")