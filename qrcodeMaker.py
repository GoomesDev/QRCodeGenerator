import qrcode
import time

print('\nQRCode Generator // Made by GoomesH\n')

time.sleep(1)

link = input('Enter the URL you want:')

time.sleep(1)

img = qrcode.make(link)

title = input('\nNow enter a name for your QRCode:')

time.sleep(1)

img.save(title + '.png')

print('\nYour QRCode is ready! Take a look at the project folder!\n')

time.sleep(1)

