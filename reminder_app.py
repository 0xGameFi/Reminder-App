# reminder_app.py

import time

def set_reminder(message, seconds):
    time.sleep(seconds)
    print("Reminder:", message)

# Sample usage
set_reminder("Take a break!", 10)
