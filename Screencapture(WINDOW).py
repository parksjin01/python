import PIL.ImageGrab
import os

a=PIL.ImageGrab.grab()
print a.show
a.save('testtest.png')
os.system('Pause')
