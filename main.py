#DISPLAY variable for pyautogiu
import os
os.environ['DISPLAY'] = ':0'

from TrackerFunc import *

x = Tracker()
x.LandingPageChecker()


#from TEST import *
#test = TrackerTest()
#test.LandingPageChecker()