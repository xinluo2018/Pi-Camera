from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous('img_{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
    print('Captured %s' % filename)
    sleep(10)  
