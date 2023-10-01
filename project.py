# import qrcode as qr
# img= qr.make("https://web.whatsapp.com/")
# img.save("my_whatsapp.png")

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.youtube.com/@ApnaCollegeOfficial")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("apna_college.png")