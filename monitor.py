#!/usr/bin python

import sys
import push

# Change threshold based on requirements
THRESHOLD = 0.01

# Pushover credentials (optional)
PUSHOVER_USER_KEY = ""
PUSHOVER_API_KEY = ""

# Variables for suppressing notifications for 10 seconds after a trigger
count = 0
suppress = False

# Main loop
while True:
    try:
        # Receive audio level from stdin
        line = sys.stdin.readline().strip()  # e.g. "0.006543"
        number = float(line)
        if number > THRESHOLD and not suppress:
            p = push.PushoverSender(PUSHOVER_USER_KEY, PUSHOVER_API_KEY)
            p.send_notification("A noise has been detected!")
            count = 0
            suppress = True
        else:
            print("All quiet")
            
        # Count 5 cycles after a trigger
        if suppress:
            count += 1
        if count >= 5:
            count = 0
            suppress = False
            
    # Value error
    except ValueError:
        # Cannot coerce to float or error in stdin
        print("Value error: " + line)
        break
    
    # Keyboard interrrupt
    except KeyboardInterrupt:
        # Cancelled
        print("Baby monitor script ending")
        break

# Exit
sys.exit()
