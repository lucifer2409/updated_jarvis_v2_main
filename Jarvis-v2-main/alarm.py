from win10toast import ToastNotifier
import datetime
import time

def set_alarm(alarm_time):
    # get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # calculate the number of seconds until the alarm time
    time_diff = (datetime.datetime.strptime(alarm_time, "%H:%M:%S") - datetime.datetime.strptime(current_time, "%H:%M:%S")).total_seconds()

    if time_diff < 0:
        print("Invalid time entered")
        return

    # wait for the specified time
    time.sleep(time_diff)

    # show a Windows toast notification at the alarm time
    toaster = ToastNotifier()
    toaster.show_toast("Alarm", "Wake up!", duration=10, threaded=True)

set_alarm("18:29:00")