import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/channel/UCUBpKrn0GZzbRUZlP5kzTHw"

url = pyqrcode.create(s)
url.svg("myyoutube.svg", scale= 6)