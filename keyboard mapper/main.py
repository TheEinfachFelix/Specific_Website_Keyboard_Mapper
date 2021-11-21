#you have to install selenium and keyboard via pip to run itfrom selenium import webdriver
from selenium import webdriver
import time
import keyboard  

wait = 0.2
driver = webdriver.Firefox()

#Enter the wepsids address here
driver.get('')
time.sleep(4)

while True:
    #stop
    if keyboard.is_pressed('Escape'):
        exit()

    #Senden
    if keyboard.is_pressed('Space'):
        send = driver.find_element_by_xpath("/html/body/form/input[20]")
        send.submit()
        time.sleep(wait)
    
    ###Löschen
    if keyboard.is_pressed('a'):
        driver.find_element_by_id("kat_-1").click()
        time.sleep(wait)
    #Anime
    if keyboard.is_pressed('s'):
        driver.find_element_by_id("kat_4").click()
        time.sleep(wait)
    #Aussagen
    if keyboard.is_pressed('d'):
        driver.find_element_by_id("kat_12").click()
        time.sleep(wait)
    #Beleidigungen
    if keyboard.is_pressed('f'):
        driver.find_element_by_id("kat_3").click()
        time.sleep(wait)
    #Clientsounds
    if keyboard.is_pressed('g'):
        driver.find_element_by_id("kat_16").click()
        time.sleep(wait)
    #CSGO
    if keyboard.is_pressed('h'):
        driver.find_element_by_id("kat_14").click()
        time.sleep(wait)
    #Drama
    if keyboard.is_pressed('j'):
        driver.find_element_by_id("kat_8").click()
        time.sleep(wait)
    #Flöte
    if keyboard.is_pressed('k'):
        driver.find_element_by_id("kat_15").click()
        time.sleep(wait)
    #Monte
    if keyboard.is_pressed('l'):
        driver.find_element_by_id("kat_2").click()
        time.sleep(wait)
    #Mucke
    if keyboard.is_pressed('ö'):
        driver.find_element_by_id("kat_1").click()
        time.sleep(wait)
    #Sound
    if keyboard.is_pressed('ä'):
        driver.find_element_by_id("kat_7").click()
        time.sleep(wait)
    

    #Game
    if keyboard.is_pressed('e'):
        driver.find_element_by_id("kat_11").click()
        time.sleep(wait)
    #Spongebob
    if keyboard.is_pressed('r'):
        driver.find_element_by_id("kat_10").click()
        time.sleep(wait)
    #Stromberg
    if keyboard.is_pressed('t'):
        driver.find_element_by_id("kat_9").click()
        time.sleep(wait)
    #Film Audio
    if keyboard.is_pressed('z'):
        driver.find_element_by_id("kat_5").click()
        time.sleep(wait)
    #Trump
    if keyboard.is_pressed('u'):
        driver.find_element_by_id("kat_6").click()
        time.sleep(wait)
    #Werbung
    if keyboard.is_pressed('i'):
        driver.find_element_by_id("kat_13").click()
        time.sleep(wait)
