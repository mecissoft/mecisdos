import time
import os
from datetime import datetime

os.system('clear')
print("Welcome to ")
print("   __  __           _     _____   ____   _____ ")
print(" |  \/  |         (_)   |  __ \ / __ \ / ____|")
print(" | |\/| |/ _ \/ __| / __| |  | | |  | |\___ \  ")
print(" | |  | |  __/ (__| \__ \ |__| | |__| |____) |")
print(" |_|  |_|\___|\___|_|___/_____/ \____/|_____/ ")
print("Linux Editon")
time.sleep(2)
now = datetime.now()

current_time = now.strftime("%H:%M")
print("Time is " +current_time)
print("Loading...")
time.sleep(0.2)
RAM = input("How many you have GB in RAM?: ")
ROM = input("How many you have GB in SSD or HDD?: ")
print("RAM:" +RAM +"GB")
print("ROM:" +ROM +"GB")
time.sleep(0.2)
print("One little bit...")
time.sleep(1)
os.system('clear')
print("Welcome to MecisDOS 11.0 Linux Edition!. this is dos adapted to run on modern os's.")
while True:
    com1 = input("/")
    if com1 == "test":
        print("Test command")
    if com1 == "ver":
        print("   __  __           _     _____   ____   _____ ")
        print(" |  \/  |         (_)   |  __ \ / __ \ / ____|")
        print(" | |\/| |/ _ \/ __| / __| |  | | |  | |\___ \  ")
        print(" | |  | |  __/ (__| \__ \ |__| | |__| |____) |")
        print(" |_|  |_|\___|\___|_|___/_____/ \____/|_____/ ")
        print("MecisDOS 11.0 Linux Edition")
        print("©MECIS Software And XDAFAD Software.")
    if com1 == "exit":
        os.system('exit')
        break
    if com1 == "clear":
        os.system('clear')
    if com1 == "reset":
        os.system("python dos.py")
        break
    if com1 == "ls":
        os.system("ls")
    if com1 == "help":
        print ("comands:")
        print ("help - comands             dir - view files on this dir")
        print ("reset - restart the dos    clear - clear all message on the dos")
        print ("test - test command         exit - exit the dos")
        print ("ver - version              sysinfo - your system info")
        print ("info - DOS Information      authors - DOS Authors")
        print ("echo - repeats words   notepad - opening windows notepad")
        print ("time - shows the time  vk - Mecis VK Group")
    if com1 == "authors":
        print ("Nikita Rojdestvin - Versions until 8.0.1")
        print ("Artem Litvinsev - Versions from 8.1. MECIS Software Owner")
        print ("Seva Tretyakov - Coder. XDAFAD Software Owner")
    if com1 == "info":
        print("MecisDOS is a DOS without installing By Mecis Software. you must be write in cmd or terminal python dos.py and it starts.")

    if com1 == "sysinfo":
        proc = input("What Proccesor do you have? ")
        time.sleep(0.1)
        print("OS: MecisDOS 11.0 Linux Edition")
        print("Proccesor: " +proc)
        print("ROM: " +ROM +"GB")
        time.sleep(0.1)
        print("RAM: " +RAM +"GB")
    if com1 == "kakish":
        print("ugh. ugh. ugh.")
    if com1 == "color green":
        os.system("color 2")
    if com1 == "color blue":
        os.system("color 1")
    if com1 == "color gray":
        os.system("color 8")
    if com1 == "term":
        com = input("what command do you need?: ")
        os.system(com)
    if com1 == "echo":
        word = input("what word do you need?: ")
        os.system("echo " +word)
    if com1 == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time: ", current_time)
    if com1 == "mecis":
        print("https://vk.com/mecissoft")


        
