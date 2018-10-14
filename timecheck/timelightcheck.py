import cv2
import datetime

class TimeLightCheck:

    def __init__(self):
        print('Light checker initialized')

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

        if avg < 50:
            lightlevel = 0
        else:
            lightlevel = 1  
        return lightlevel

    # compares the current time to the time classed as night time
    def timecheck(self):
        #now = datetime.datetime.now().time() # time right now
        now = datetime.time(hour=23)
        if datetime.time(hour=22) <= now or now <= datetime.time(hour=3):
            day = 0
        else:
            day = 1
        return day
    
    def bedtime(self, light_output):
        self.lightlevel = self.brightness()
        self.day = self.timecheck()
        if self.lightlevel == 1 and self.day == 0:
            light_output.put("I see you're up late again. I'm calling your mother.")
        else:
            light_output.put(None)