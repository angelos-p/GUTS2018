import cv2
import datetime

class TimeLightCheck:

    def __init__(self):
        lightlevel = self.brightness()
        day = self.timecheck()
        self.bedtime(lightlevel,day)

    def brightness(self):
        cam = cv2.VideoCapture(0)
        ret_val, img = cam.read()
        rows = img.shape[0]
        cols = img.shape[1]

        # grayscale conversion
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sum = 0
        for m in range(rows):
            for n in range(cols):
                sum = sum + gray[m,n]
        
        avg = sum/(rows*cols)

        if avg < 128:
            lightlevel = 0
        else:
            lightlevel = 1  
        return lightlevel

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