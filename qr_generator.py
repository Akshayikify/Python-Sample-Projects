import qrcode

url=input("Enter the url : ")

trimmed_url=url.strip()

img=qrcode.make(trimmed_url)

img.save('QRCode image.png')
