from win10toast import ToastNotifier
import time

REAPEAT_INTERVAL= 10
while True:
 def display_notification(title, message):
    
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)
    time.sleep(REAPEAT_INTERVAL)

 if __name__ == "__main__":
    notification_title = "Drink water"
    notification_message = "its time for water now"
    display_notification(notification_title, notification_message)
