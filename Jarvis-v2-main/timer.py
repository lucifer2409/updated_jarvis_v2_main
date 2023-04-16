import time
import winsound
import threading

def set_timer(minutes, seconds):
    # convert minutes to seconds and add to seconds argument
    duration = minutes * 60 + seconds
    # wait for the specified duration
    print(time.sleep(duration))
    time.sleep(duration)
    
    # play a sound
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    
    # display a notification
    threading.Thread(target=display_notification, args=("Timer Complete",)).start()

def display_notification(message):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast("Timer", message, duration=5)

# example usage: set a timer for 1 minute and 30 seconds
set_timer(1, 30)
