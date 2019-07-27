import pyqrcode

name = "Purushotham Reddy"

url = pyqrcode.create(name)

url.svg("myqr.svg",scale=8)
