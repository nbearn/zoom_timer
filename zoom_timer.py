# required permissions: give Terminal record and keyboard/mouse access
# System Preferences > Security & Privacy > Privacy tab
# - Accessibility
# - Full Disk Access
# - Automation
# give "/usr/sbin/cron" Full Disk Access & Accessibility as well
#
# Waking Laptop from sleep
# Cannot set multiple wake up times, so use root user's crontab to chain the wake up times
# sudo crontab -e
# 55 7 * * * pmset repeat wakeorpoweron MTWRFSU 17:53:00 # @ 7:55am set wakeup to 5:53pm
# 55 17 * * * pmset repeat wakeorpoweron MTWRFSU 07:53:00 # @ 5:55pm set wakeup to 7:53am
import os
import time
import argparse
import webbrowser
import pyautogui

pyautogui.FAILSAFE = False

QUICKTIME_CMD = "open -a 'QuickTime Player'"
ZOOM_CMD = "open -a 'zoom.us'"
TIME_MULTIPLIER = 60
# Feldenkrais daily
ZOOM_LINK = "https://us02web.zoom.us/j/83037293331?pwd=amtZaXUvQUVvdHRFTmpZa0VWVWgrZz09"
QUICKTIME_APPLESCRIPT = """
tell application "QuickTime Player"
    new screen recording
end tell
"""

SLEEP_TIME = 10

def focus_on(app_name):
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Focusing on {app_name} ", flush=True)

    time.sleep(SLEEP_TIME)
    os.system(f"osascript -e 'tell application \"{app_name}\" to activate'")
    time.sleep(SLEEP_TIME)

def record():
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Starting Record ", flush=True)

    os.system(f"osascript -e '{QUICKTIME_APPLESCRIPT}'")
    #with pyautogui.hold(['command', 'shift']):
    #   pyautogui.press('5')
    time.sleep(SLEEP_TIME)
    pyautogui.press('enter')
    time.sleep(SLEEP_TIME)

def open_zoom(zoom_url):
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Opening Zoom ", flush=True)

    # open Zoom
    webbrowser.open_new_tab(zoom_url)
    time.sleep(SLEEP_TIME)

    # move mouse out of the way
    screen_size = pyautogui.size()
    pyautogui.moveTo(screen_size[0], 100)

    # open Zoom chat
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Opening Zoom Chat ", flush=True)
    focus_on("zoom.us")
    with pyautogui.hold(['command', 'shift']):
        pyautogui.press('h')

    time.sleep(SLEEP_TIME)

    # open Zoom Participants 
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Opening Zoom Participants ", flush=True)
    focus_on("zoom.us")
    with pyautogui.hold(['command']):
        pyautogui.press('u')

    time.sleep(SLEEP_TIME)

    # move mouse to click on "Got it" for "You are chatting as a guest"
    screen_size = pyautogui.size()
    pyautogui.click(1596,811)

    time.sleep(SLEEP_TIME)

def zoom_record():
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Using Zoom built in record function ", flush=True)
    
    time.sleep(SLEEP_TIME)
    time.sleep(SLEEP_TIME)

    pyautogui.click(1597,481)
    pyautogui.press('9')
    pyautogui.press('9')
    pyautogui.press('3')
    pyautogui.press('0')
    pyautogui.press('5')
    pyautogui.press('5')
    pyautogui.press('enter')
    
    # sleep 
    time.sleep(SLEEP_TIME)

    # shift - cmd - r
    with pyautogui.hold(['command', 'shift']):
        pyautogui.press('r')

    # click on the "you are muted" "Record Without Audio"
    time.sleep(SLEEP_TIME)
    pyautogui.click(842,352) 

    time.sleep(SLEEP_TIME)

    pyautogui.click(265,938)
    time.sleep(SLEEP_TIME)
    pyautogui.click(323,737)

    # move mouse out of the way
    screen_size = pyautogui.size()
    pyautogui.moveTo(screen_size[0], 100)

def stop_recording():
    # stop quicktime recording
    focus_on("QuickTime Player")
    with pyautogui.hold(['command', 'ctrl']):
        pyautogui.press('esc')
    time.sleep(SLEEP_TIME)

def stop_zoom():    
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Stopping Zoom ", flush=True)
    
    # close Zoom chat
    focus_on("zoom.us")
    
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Closing Zoom chat ", flush=True)
    
    with pyautogui.hold(['command', 'shift']):
        pyautogui.press('h')
   
   # leave Zoom
    focus_on("zoom.us")
    
    if args.verbose:
       print(f"[{time.ctime()}] [VERBOSE]: Closing Zoom Window ", flush=True)
    
    with pyautogui.hold(['command']):
        pyautogui.press('w')
    time.sleep(SLEEP_TIME)
    pyautogui.press('enter')

################################################################################
################################################################################
##### START ACTUAL SCRIPT #####
# parse args
parser = argparse.ArgumentParser()
parser.add_argument("url", type=str,
                    help="url to open")
parser.add_argument("-d", "--duration", type=int, default=145,
                    help="recording duration in minutes")

parser.add_argument("-t", "--test", default=False, action='store_true',
                    help="test script, duration is measured in seconds instead of minutes")

parser.add_argument("-v", "--verbose", default=False, action='store_true',
                    help="verbose logging mode")

parser.add_argument("-r", "--zoom_record", default=False, action='store_true',
                    help="use Zoom to record")

args = parser.parse_args()

print(f"[{time.ctime()}] Recording {args.url}")
print(f"[{time.ctime()}] Test Mode: {args.test}")
print(f"[{time.ctime()}] Verbose Mode: {args.verbose}")
print(f"[{time.ctime()}] Duration: {args.duration} mins", flush=True)

# if test mode on, set sleep time and time multiplier to 1 
if args.test:
   TIME_MULTIPLIER = 1
   SLEEP_TIME = 1

print(f"[{time.ctime()}] Test Mode {args.test}: TIME_MULTIPLIER: {TIME_MULTIPLIER}, SLEEP_TIME: {SLEEP_TIME} ", flush=True)

#######################################################################################
################################### BEGIN #############################################
#######################################################################################
# move mouse out of the way
screen_size = pyautogui.size()
pyautogui.moveTo(screen_size[0], 100)
# move mouse out of the way
pyautogui.moveTo(screen_size[0], 120)

time.sleep(SLEEP_TIME)


# open Zoom and focus on it
open_zoom(args.url)

if args.zoom_record:
    zoom_record()
else:
    record()

# focus on Zoom again just to be sure
focus_on("zoom.us") 

# start sleep
if args.verbose:
   print(f"[{time.ctime()}] [VERBOSE]: Sleeping for {(args.duration * TIME_MULTIPLIER)} sec", flush=True)
time.sleep((args.duration * TIME_MULTIPLIER))

# quit zoom
stop_zoom()

time.sleep(SLEEP_TIME)

# stop screen recording
for stop_attempt in range(5):
   time.sleep(SLEEP_TIME)
   if args.verbose:
      print(f"[{time.ctime()}] [VERBOSE]: Stopping Recording #{stop_attempt}", flush=True)
   stop_recording()

print(f"[{time.ctime()}] Finished {args.url}", flush=True)
