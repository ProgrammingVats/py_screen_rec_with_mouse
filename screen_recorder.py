import cv2 # pip install opencv-python
import numpy as np # pip install numpy
from PIL import Image, ImageGrab, ImageDraw, ImageOps # pip install pillow
import pyautogui as pg # pip install pyautogui
import keyboard # pip install keyboard
import time 
import win32gui # pip install pywin32
import sounddevice as sd # pip install sounddevice
#import pyttsx3 # pip install pyttsx3


try:
    resolution = (16,9)
    w,h = ImageGrab.grab().size

    cursor = Image.open("images\\cursor.png")
    hand = Image.open("images\\hand.png")
    ibeam = Image.open("images\\ibeam.png").resize((15,20))
    iwidth, iheight = ibeam.size

    logo = Image.open("images\\logo_tr.png").resize((100,100))
    # logo = ImageOps.invert(logo)
    fname = input("Enter the Filename: ")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(fname, fourcc, 5.0, (w, h))
    # pyttsx3.speak("your recording is going to be started. threee...... tooooo...... one.... start")
    while True:
        screen = ImageGrab.grab()

        x = int(pg.position()[0])
        y = int(pg.position()[1])

        width, height = screen.size
        # draw = ImageDraw.Draw(img)
        # # draw.ellipse((x,y,x+20, y+20), fill=(255,100,0),outline = (0,0,0))
        img = Image.new('RGBA', (width, height), (0,0,0,50))
        img.paste(screen, (0,0))
        # img.paste(cursor, (x,y), mask=cursor)
        img.paste(logo,(width-120,height-150),mask=logo)
        e = win32gui.GetIconInfo(win32gui.GetCursorInfo()[1])
        if e[1] == 0:
            img.paste(cursor,(x,y),mask=cursor)

        elif e[1]==6:
            img.paste(hand,(x,y),mask=hand)
        elif e[1]==8:
            img.paste(ibeam,(x,y),mask=ibeam)
        else:
            img.paste(cursor,(int(x-(iwidth/2)),int(y-(iheight/2))),mask=cursor)


        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("hey", frame)
        
        out.write(frame)
        if cv2.waitKey(1) & keyboard.is_pressed("esc"):
            break

    out.release()
    cv2.destroyAllWindows()
    # pyttsx3.speak("your recording is done!")

except Exception as e:
    print(f"your recording could not be completed because of{e}")
