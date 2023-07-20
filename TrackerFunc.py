# for TrackerFunc()
import pymouse
import time

# Message Box
from tkinter import *
from tkinter import messagebox

# for browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# for browser-URL-check
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# for refresh_webseite() 
import pyautogui
import subprocess


import os
os.environ['DISPLAY'] = ':0'

from subprocess import *


class Tracker:
    
    mousePosCurrent = [0,0]
    killTracker = True
    timeToWait = 2 # secconds to wait till next mouse snapshot
    
    def MouseTracker(self):
        """Sets Mouseposition (x,y) initially and tracks movements.
            No movement activates *noActivity_TextBox()*"""
        mousePosOne = pymouse.PyMouse()
        self.mousePosCurrent[0] = mousePosOne.position()[0]
        self.mousePosCurrent[1] = mousePosOne.position()[1]
        
        while self.killTracker:       
            time.sleep(self.timeToWait)
            mousePosTwo = pymouse.PyMouse()
            
            if self.mousePosCurrent[0] != mousePosTwo.position()[0] or self.mousePosCurrent[1] != mousePosTwo.position()[1]: 
                print("YOU MOVED")
                self.mousePosCurrent[0] = mousePosTwo.position()[0]
                self.mousePosCurrent[1] = mousePosTwo.position()[1]
            
            else:
                print("YOU DID NOTHING ... .sleep()")
                self.killTracker = False
                time.sleep(15) #Seconds to wait for unactive user
                self.noActivity_TextBox()  
         
         
    
    def refresh_webseite(self):
        """Refreshes/Loads landingpage in kiosk mode to specific URL and closes browser """
        
        try:
            print("tab closed and refresh website...")
            pyautogui.hotkey('ctrl', 'w') 
        finally:
            #driver = webdriver.Chrome()
            #driver.get("https://zimmergroup.sharepoint.com/SitePages/infoboard.aspx")
            #driver.fullscreen_window()
            subprocess.call(['sh', '/home/zimmerpi/Desktop/ActivityTrackerProgram/OpenWebsite.sh'])
            self.LandingPageChecker()        
    
       
       

    # show message 
    def noActivity_TextBox(self):
        #self.killTracker = False        
        #time.sleep(60) #Wait for a few secconds to continue
        window = Tk()
        window.wm_withdraw() #to hide the main window
        
        try:
            window.after(10000, window.destroy)#Destroy window after 10 seconds if not react with "yes" or "no"
            noUserOnScreen = False
            if messagebox.askyesno('Zimmer Infoboard', 'Auf der Seite bleiben um weiterzulesen?') == False:
                #NO, go back to landing-page
                window.destroy()
                noUserOnScreen = True
                self.refresh_webseite()
                
            else:
                # Yes, track further
                window.destroy()
                noUserOnScreen = True
                self.killTracker = True 
                self.MouseTracker()
                
        finally:
            # start tracking again if no interaction from user
            if noUserOnScreen == False:
                self.refresh_webseite()
               
        
       

    # checks activity at landingpage
    def LandingPageChecker(self):
        """Checks for activity on landingpage.
        No movement == stay.
        Movement == activate *MouseTracker()*"""
        
        print("LandingPageTRACKER STARTET....")
        
        CurrentLandPageMouse = [0,0]
        timeToWait = 3 # How long wait to check next time
        x = Tracker()
        
        mousePosOne = pymouse.PyMouse()
        CurrentLandPageMouse[0] = mousePosOne.position()[0]
        CurrentLandPageMouse[1] = mousePosOne.position()[1]
        killLoop = True
        
        while killLoop:       
            time.sleep(timeToWait)
            mousePosTwo = pymouse.PyMouse()
           
            if CurrentLandPageMouse[0] != mousePosTwo.position()[0] or CurrentLandPageMouse[1] != mousePosTwo.position()[1]: 
                print("SCREEN TOUCHED")
                killLoop = False
                x.MouseTracker()
            
            else:
                print("SCREEN NOT TOUCHED") 
        
        