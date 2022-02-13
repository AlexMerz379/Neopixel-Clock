#
#Clock.py
#
#Autor: Alex Merz
#


#Libraries
import time
from neopixel import *
import datetime


#LED strip configuration:
LED_COUNT      = 170     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


#Instantiate Class
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()


#Local variable
ActualTimeOld = 0
GreenOld = 255
RedOld = 0
BlueOld = 0
BrightnessOld = 100
StatusOld = False


#Local const
Nbr0 = [1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0] #Segment splitted in A,B,C,D,E and F parts
Nbr1 = [0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0] #Segment splitted in A,B,C,D,E and F parts
Nbr2 = [1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
Nbr3 = [1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   0,0,0,0,0,0,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
Nbr4 = [0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
Nbr5 = [1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
Nbr6 = [1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
Nbr7 = [1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0] #Segment splitted in A,B,C,D,E and F parts
Nbr8 = [1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
Nbr9 = [1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts

LetterA = [1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
LetterL = [0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0] #Segment splitted in A,B,C,D,E and F parts
LetterE = [1,1,1,1,1,1,   0,0,0,0,0,0,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
LetterX = [0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
LetterH = [0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   1,1,1,1,1,1] #Segment splitted in A,B,C,D,E and F parts
LetterI = [0,0,0,0,0,0,   1,1,1,1,1,1,   1,1,1,1,1,1,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0] #Segment splitted in A,B,C,D,E and F parts
Nothing = [0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0,   0,0,0,0,0,0] #Segment splitted in A,B,C,D,E and F parts

S1Start = 0
S1End   = 41
S2Start = 42
S2End   = 83
S3Start = 84
S3End   = 125
S4Start = 126
S4End   = 167
Dot1    = 168
Dot2    = 169


####################Function: GetNbrArray
def GetNbrArray(Number=0):
	if Number == 0:
		return Nbr0
	if Number == 1:
		return Nbr1
	if Number == 2:
		return Nbr2
	if Number == 3:
		return Nbr3
	if Number == 4:
		return Nbr4
	if Number == 5:
		return Nbr5
	if Number == 6:
		return Nbr6
	if Number == 7:
		return Nbr7
	if Number == 8:
		return Nbr8
	if Number == 9:
		return Nbr9


####################Function: ClearSegment
def ClearSegment(strip):
	for i in range(S1Start, S4End):
		strip.setPixelColorRGB(i, 0,0,0) #Clear
	strip.show()


####################Function: SetSegment
def SetSegment(strip, color, S1=[1], S2=[1], S3=[1], S4=[1], wait_ms=0):
	#Color = Green, Red, Blue

	ClearSegment(strip)
	strip.setPixelColorRGB(Dot1, 0, 0, 0)
	strip.setPixelColorRGB(Dot2, 0, 0, 0)

	for i in range(0, 42):
		if S1[i] == 1:
			strip.setPixelColor(i, color)
		else:
			strip.setPixelColorRGB(i, 0,0,0)
		if wait_ms > 0:
			strip.show()
			time.sleep(wait_ms/1000.0)

	for i in range(0, 42):
		if S2[i] == 1:
			strip.setPixelColor((S2Start+i), color)
		else:
			strip.setPixelColorRGB((S2Start+i), 0,0,0)
		if wait_ms > 0:
			strip.show()
			time.sleep(wait_ms/1000.0)

	for i in range(0, 42):
		if S3[i] == 1:
			strip.setPixelColor((S3Start+i), color)
		else:
			strip.setPixelColorRGB((S3Start+i), 0,0,0)
		if wait_ms > 0:
			strip.show()
			time.sleep(wait_ms/1000.0)

	for i in range(0, 42):
		if S4[i] == 1:
			strip.setPixelColor((S4Start+i), color)
		else:
			strip.setPixelColorRGB((S4Start+i), 0,0,0)
		if wait_ms > 0:
			strip.show()
			time.sleep(wait_ms/1000.0)

	if wait_ms == 0:
		strip.show()


####################Function: Startup
def Startup():
	SetSegment(strip, Color(255, 0, 0), LetterH, LetterI, Nothing, Nothing, 10)
	time.sleep(2) #Wait 2 second
	SetSegment(strip, Color(0, 0, 255), LetterA, LetterL, LetterE, LetterX, 10)
	time.sleep(2) #Wait 2 second


####################Function: ClockControl (Main)
def ClockControl(Green=255, Red=0, Blue=0, Brightness=100, Status=True):
	global ActualTimeOld
	global GreenOld
	global RedOld
	global BlueOld
	global BrightnessOld
	global StatusOld

	ActualTime = datetime.datetime.now() #Get actual time

	#####Set segment
	if ActualTime.minute != ActualTimeOld:
		SetSegment(strip, Color(Green, Red, Blue), 
				GetNbrArray(abs(ActualTime.hour/10)), 
				GetNbrArray(ActualTime.hour%10), 
				GetNbrArray(abs(ActualTime.minute/10)), 
				GetNbrArray(ActualTime.minute%10))

		strip.setPixelColorRGB(Dot1, Green, Red, Blue)
		strip.setPixelColorRGB(Dot2, Green, Red, Blue)

		strip.show()
		ActualTimeOld = ActualTime.minute
	elif (Green != GreenOld) or (Red != RedOld) or (Blue != BlueOld):
		SetSegment(strip, Color(Green, Red, Blue), 
				GetNbrArray(abs(ActualTime.hour/10)), 
				GetNbrArray(ActualTime.hour%10), 
				GetNbrArray(abs(ActualTime.minute/10)), 
				GetNbrArray(ActualTime.minute%10))

		strip.setPixelColorRGB(Dot1, Green, Red, Blue)
		strip.setPixelColorRGB(Dot2, Green, Red, Blue)

		strip.show()
		GreenOld = Green
		RedOld = Red
		BlueOld = Blue
	elif Brightness != BrightnessOld:
		strip.setBrightness(Brightness)
		strip.show()
		
		BrightnessOld = Brightness
	elif Status != StatusOld:
		if Status == True:
			strip.setBrightness(Brightness)
		else:
			strip.setBrightness(0) #Turn strip off

		strip.show()
		StatusOld = Status

	time.sleep(1) #Wait 1 second, because of too much processor load

