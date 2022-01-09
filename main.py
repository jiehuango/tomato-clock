import time
import threading
import tkinter as tk
from tkinter import ttk

def exit_clock():
    exit(0)

def wait_minutes():
    messageTk.withdraw()
    timer=threading.Timer((5*60), wait_time_over)
    timer.start()
    

def wait_time_over():
    print ("OK!")
    clock(25*60)

def time_over():
    print("Time Over")
    global messageTk
    messageTk=tk.Tk()
    messageTk.update()
    timeover = tk.Label(messageTk,text="Time over.Do you want to wait 5 minutes?")
    timeover.pack()
    yesB = tk.Button(messageTk,text="Yes",command=wait_minutes)
    noB = tk.Button(messageTk,text="No",command=exit_clock)
    yesB.pack()
    noB.pack()
    messageTk.mainloop()

def clock(muchtime):
    
    timer=threading.Timer(muchtime, time_over)
    timer.start()

print("Tomato-clock is start!")
clock(25*60)


