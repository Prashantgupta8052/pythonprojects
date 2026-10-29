import qrcode
import qrcode.constants

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=15,
                border=8)
qr.add_data("https://github.com/Prashantgupta8052")
qr.make(fit=True)
img=qr.make_image(fill_color="darkblue",back_color="white")
img.save("github_qr.png")