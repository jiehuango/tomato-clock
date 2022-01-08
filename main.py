import time
import threading

def time_over():     
    print("Time Over")


def clock(muchtime):
    timer=threading.Timer(muchtime, time_over)
    timer.start()

clock(25*60)


