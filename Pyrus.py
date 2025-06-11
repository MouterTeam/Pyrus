# pyrus = python + virus

import time  # gia diafora "perimene" sto programma mas
import pyautogui as pg  # elegxei keyboard + mouse
import winsound  # paizei .wav hxous
import os, sys  # gia na exoume prosvasi sta windows (os) kai se diafores leitourgies tou upologisti (sys)
import tkinter as tk  # gia dimourgia parathirou me eikones, koumpia k.a.
from PIL import Image, ImageTk  # gia tin eisagwgi eikonwn sto programma


run = 0

def resource_path(relative_path):
    # prosarmozei to path pou tha valei tis eikones kai tous hxous
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def updateImg(imgNum, duration):  # updateImg(3,5) -> tha fortwsei to bsod3.png gia 5 sec
    img = "bsod" + str(imgNum) + ".png"
    i = Image.open(resource_path(img)).resize((win.winfo_screenwidth(), win.winfo_screenheight()), Image.LANCZOS)
    # Image.LANCZOS einai o algorithmos/tropos me ton opoio tha ginei resize h eikona
    bg2 = ImageTk.PhotoImage(i)
    bglbl.configure(image=bg2)
    bglbl.image = bg2
    win.update()
    time.sleep(duration)

def virus(event):
    global run
    if run == 0:
     run = 1
     time.sleep(1)
     updateImg(1, 3)
     updateImg(2, 3)
     updateImg(3, 3)
     updateImg(4, 3)
     updateImg(5, 3)
     updateImg(6, 3)
     updateImg(7, 3)
     updateImg(8, 3)
     updateImg(9, 5)
     updateImg(10, 5)
     updateImg(11, 5)
     updateImg(12, 5)

def disable():
    pass



time.sleep(1)
pg.hotkey("win", "d")
dir = os.path.dirname(os.path.abspath(sys.argv[0]))  # mas dinei to path pou vrisketai auto to script
print(dir)
time.sleep(1)
im = pg.screenshot("desktop.png")
win = tk.Tk() # dimiourgia extra parathurou
win.geometry("{}x{}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))  # ruthmizoume tis diastaseis tou parathyrou
# "1920 x 1080 + 0 + 0"
# print(win.winfo_screenwidth())
# print(win.winfo_screenheight())
bg = tk.PhotoImage(file = "desktop.png")
bglbl = tk.Label(win, image=bg, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
bglbl.place(x=0, y=0, width=win.winfo_screenwidth(), height=win.winfo_screenheight())

bglbl.bind('<Button-1>', virus)
win.attributes("-fullscreen", True) # gia na piasei to parathyro oli tin othoni
win.attributes("-topmost", True) # gia na einai mprosta apo ta upoloipa parathira
win.bind('<Escape>', disable) # lew sto ESC na min kanei tipota
win.protocol("WM_DELETE_WINDOW", disable) # lew sto ALT+F4 na min kanei tipota
win.update()

win.mainloop() # PANTA sto telos otan xrisimopoioume tin vivliothiki tkinter