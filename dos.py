import time
import os

os.system('cls')
print("  _____         _     ____  _____ _____")
print("|     |___ ___|_|___|    \|     |   __|")
print("| | | | -_|  _| |_ -|  |  |  |  |__   ")
print("|_|_|_|___|___|_|___|____/|_____|_____|")
time.sleep(2)
print("LOADING...")
time.sleep(0.2)
RAM = input("How many you have GB in RAM?: ")
ROM = input("How many you have GB in SSD or HDD?: ")
print("RAM:" +RAM +"GB")
print("ROM:" +ROM +"GB")
time.sleep(0.2)
print("One little bit...")
time.sleep(1)
os.system('cls')
print("Welcome to MecisDOS! 10.0 this is dos adapted to run on modern os's. This project use GENERAL PUBLIC LICENCE V3.0")
while True:
    com1 = input("C:/>")
    if com1 == "test":
        print("Test command")
    if com1 == "ver":
        print("  _____         _     ____  _____ _____")
        print("|     |___ ___|_|___|    \|     |   __|")
        print("| | | | -_|  _| |_ -|  |  |  |  |__   ")
        print("|_|_|_|___|___|_|___|____/|_____|_____|")
        print("MecisDOS 10.0")
        print("©MECIS Software And XDAFAD Software.")
    if com1 == "exit":
        os.system('cls')
        break
    if com1 == "clear":
        os.system('cls')
    if com1 == "reset":
        os.system("python dos.py")
        break
    if com1 == "dir":
        os.system("dir")
    if com1 == "help":
        print ("comands:")
        print ("help - comands             dir - view files on this dir")
        print ("reset - restart the dos    clear - clear all messege on the dos")
        print ("test - test comand         exit - exit the dos")
        print ("ver - version              sysinfo - your system info")
        print ("info - DOS Information      authors - DOS Authors")
        print ("color green,blue or gray - making DOS green, blue and gray!")
        print ("echo - repeats words   notepad - opening windows notepad")
    if com1 == "authors":
        print ("Nikita Rojdestvin - Versions until 8.0.1")
        print ("Artem Litvinsev - Versions from 8.1. MECIS Software Owner")
        print ("Seva Tretyakov - Coder. XDAFAD Software Owner")
    if com1 == "info":
        print("MecisDOS is a DOS without installing. you must be write in cmd or terminal python dos.py and it starts.")

    if com1 == "sysinfo":
        proc = input("What Proccesor do you have? ")
        time.sleep(0.1)
        print("OS: MecisDOS 10.0")
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
    if com1 == "notepad":
        os.system("notepad")
    if com1 == "echo":
        word = input("what word do you need?: ")
        os.system("echo " +word)