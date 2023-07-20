from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

import pymouse
import time



#s=Service('/usr/bin/chromedriver')
#driver = webdriver.Chrome(service=s)
#def refresh_webseite(self):
    #s=Service('/usr/bin/chromedriver')
    #driver = webdriver.Chrome(service=s)
#    driver.get("https://zimmergroup.sharepoint.com/SitePages/infoboard.aspx")
#    sleep(10)
    #driver.close()



#from TrackerFunc import *


#def LandingPageChecker():   
#    CurrentLandPageMouse = [0,0]
#    killTracker = True
#    timeToWait = 3 # How long to wait to check next time
    
#    x = Tracker()
#    mousePosOne = pymouse.PyMouse()
#    CurrentLandPageMouse[0] = mousePosOne.position()[0]
#    CurrentLandPageMouse[1] = mousePosOne.position()[1]
        
#    while killTracker:       
#        time.sleep(timeToWait)
#        mousePosTwo = pymouse.PyMouse()
            
#        if CurrentLandPageMouse[0] != mousePosTwo.position()[0]: 
#            print("SCREEN TOUCHED")
#            x.MouseTracker()
            #self.mousePosCurrent[0] = mousePosTwo.position()[0]
            
#        elif CurrentLandPageMouse[1] != mousePosTwo.position()[1]:
#            print("SCREEN TOUCHED")
#            x.MouseTracker()
            #self.mousePosCurrent[1] = mousePosTwo.position()[1]
            
#        else:
#            print("SCREEN NOT TOUCHED")                
 
 

    
    
    
           
           
# ALTE VERSION MIT URL CHECK        
    #landingPageURL = "https://zimmergroup.sharepoint.com/SitePages/infoboard.aspx"
    #wait = WebDriverWait(driver, 2) # , 10
    
    #onLandingPage = True
    
    #while onLandingPage:
        #if  driver.current_url == landingPageURL:
            #time.sleep(5)
        #else:
            #onLandingPage = False
            #x = Tracker()
            #x.MouseTracker()
            #starte aktivitätstracker
           
           
           
           
           
    
    #wait.until(EC.title_is("https://zimmergroup.sharepoint.com/SitePages/infoboard.aspx"))








    # show message 
#    def noActivity_TextBox(self):
#        time.sleep(5) # secconds to wait till user have to interact
#        self.killTracker = False
#        startTime = time.perf_counter()
#        maxTime = 5000
        
#        while startTime < maxTime:
#            window = Tk()
#            window.wm_withdraw() #to hide the main window    
#            reaction = messagebox.askyesno('Zimmer Infoboard', 'Auf der Seite bleiben um weiterzulesen?')
        
#            if reaction == False:
                #NO or "x", go back to landing-page
#                window.destroy()
#                self.refresh_webseite()
                #LandingPageChecker() #start landingpage tracker again
         
    # hier muss noch ein timer rein falls keiner auf "NEIN" drückt muss trotzdem zurück auf die landingpage
#            else:
                # Yes, track again
                #window.after(5000, window.destroy())
#                print("TRACKER STARTET....")
#                self.killTracker = True
#                window.destroy()        
        
            # start tracking again
#            self.MouseTracker()
        
# window.after(5000, window.destroy)





#setter = True
#startTime = time.time()

#while setter:
#    window = Tk()
#    window.wm_withdraw() #to hide the main window    
#    reaction = messagebox.askyesno('Zimmer Infoboard', 'Auf der Seite bleiben um weiterzulesen?')   
    
#    time.sleep(5)
#    endTime = time.time()
#    if endTime - startTime:
#    print("MACH WAS WENN DU ÜBER 5 SEKUNDEN BIST")
#    setter = False




# ALT
    # show message 
#    def noActivity_TextBox(self):
#        time.sleep(5)
        #Waits for a few secconds for continue
#        self.killTracker = False
        
#        window = Tk()
#        window.wm_withdraw() #to hide the main window    
#        reaction = messagebox.askyesno('Zimmer Infoboard', 'Auf der Seite bleiben um weiterzulesen?')
        
        #startTime = time.perf_counter()
#        startTime = time.time()
        
#        if reaction == False:
            #NO or "x", go back to landing-page
#            window.destroy()
#            self.refresh_webseite()
#            LandingPageChecker() #start landingpage tracker again
         
    # hier muss noch ein timer rein falls keiner auf "NEIN" drückt muss trotzdem zurück auf die landingpage
#        else:
            # Yes, track again
            #window.after(5000, window.destroy())
#            print("TRACKER STARTET....")
#            self.killTracker = True
#            window.destroy()        
        
        # start tracking again
#        self.MouseTracker()



#from tkinter import *
#from tkinter import messagebox

#def noActivity_TextBox():
#    time.sleep(5)
    #Waits for a few secconds for continue
#    killTracker = False
    
#    try:    
#        window = Tk()
#        window.wm_withdraw() #to hide the main window    
#        window.after(3000, window.destroy)
        
        
#        if messagebox.askyesno('Zimmer Infoboard', 'Auf der Seite bleiben um weiterzulesen?') == False:
            #NO or "x", go back to landing-page
#            window.destroy()
#            self.refresh_webseite()
#            LandingPageChecker() #start landingpage tracker again
         
#        else:
            # Yes, track again
#            print("TRACKER STARTET....")
#            self.killTracker = True
#            window.destroy()        
        
        # start tracking again
#        self.MouseTracker()
    
#    except:
#        print("TEST")

#noActivity_TextBox()

#import pyautogui
#def open_close():
#    driver = webdriver.Chrome()
#    driver.get("http://www.google.de")
#    time.sleep(5)
#    pyautogui.hotkey('ctrl', 'w')
#    print("tab closed")

#open_close()


# AKTUELL
#from selenium import webdriver

#driver = webdriver.Chrome()

#driver.get("http://www.google.de")
#driver.fullscreen_window()

from tkinter import *
from tkinter import messagebox
import asyncio





def refresh_webseite():
    """Refreshes/Loads landingpage in kiosk mode to specific URL"""
    user = "florian.dietrich@zimmer-group.com"
    password = 2
    driver = webdriver.Chrome()
    driver.get("https://zimmergroup.sharepoint.com/SitePages/infoboard.aspx")
    driver.fullscreen_window()
    LandingPageChecker()     















