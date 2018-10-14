import cv2
import datetime

class TimeLightCheck:

    def __init__(self):
        lightlevel = self.brightness()
        day = self.timecheck()
        self.bedtime(lightlevel,day)

    # Takes a picture with webcam and converts to hsv format to measure the brightness
    def brightness(self):
        cam = cv2.VideoCapture(0)
        ret_val, img = cam.read()
        rows = img.shape[0]
        cols = img.shape[1]

        # Hue, Saturation, Value conversion
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        sum = 0
        for m in range(rows):
            for n in range(cols):
                sum = sum + hsv[m,n][2]
        
        avg = sum/(rows*cols)

        if avg < 128:
            lightlevel = 0
        else:
            lightlevel = 1  
        return lightlevel

    # compares the current time to the time classed as night time
    def timecheck(self):
        now = datetime.datetime.now().time() # time right now
        if datetime.time(hour=22) <= now or now <= datetime.time(hour=3):
            day = 0
        else:
            day = 1
        return day
    
    def bedtime(self,lightlevel,day):
        if lightlevel == 1 and day == 0:
            print("Nighttime but still awake")
        else:
            print("Do nothing")

ambient = TimeLightCheck()