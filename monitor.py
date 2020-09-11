#!/usr/bin/env python

import sys
import push

THRESHOLD = 0.01 

PUSHOVER_USER_KEY = ""
PUSHOVER_API_KEY = ""

count = 0
suppress = False

while True:
    try:
        line = sys.stdin.readline().strip() # e.g. "0.006543"
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
        
    except ValueError:
        # Cannot coerce to float or error in stdin
        print("Value error: " + line)
        break
    
    except KeyboardInterrupt:
        # Cancelled
        print("Baby monitor script ending")
        break
sys.exit()


