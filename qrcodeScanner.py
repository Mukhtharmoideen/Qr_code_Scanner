import pyqrcode
import png
link = "https://www.google.com"
qr_code = pyqrcode.create(link)
qr_code.png("google.png",scale=5)
print(qr_code.terminal(module_color="black",background="white"))
