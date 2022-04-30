import os
import datetime
import time

c,b,a = input("Enter the date :").split("/")
hr,min,sec = input("Enter the time :").split(":")
shedule_date = datetime.date(int(a), int(b), int(c))

n=1
while n<0 :
    if time.localtime().tm_hour == int(hr) and time.localtime().tm_min == int(min) and time.localtime(sec).tm_sec == int(c) :
        os.startfile("C:\\Users\\himra\\PycharmProjects\\alarm_clock\\strangedrone08-impact-21849.mp3")
        break
    else :
        n = n+1
