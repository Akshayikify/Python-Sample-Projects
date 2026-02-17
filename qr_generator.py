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

