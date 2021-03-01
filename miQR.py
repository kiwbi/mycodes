import pyqrcode
import png


s = "www.instagram.com/onnisariel/'"
url = pyqrcode.create(s)
url.png('myqr.png', scale = 6)