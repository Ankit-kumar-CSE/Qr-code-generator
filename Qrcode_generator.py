import qrcode

url=input("Enter the url of which you want to generate the qr code: ").strip()
# file_path="D:\\Python\\Projects\\qrcode.png"
file_path="generated_qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print('qr code was generated: ')

