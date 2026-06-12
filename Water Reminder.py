from notifypy import Notify
import time

notification = Notify()
notification.title = "Water Reminder" 

while True:
    
    notification.message = "Hey! Please Sip some Water 💧"
    notification.send()
    time.sleep(60*60) #it will remind you to drink some water every 1 hour by giving you a notification 




