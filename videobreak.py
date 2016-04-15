##
# videobreak.py opens a youtube page every 2 hours to remind you to take a break.

import time
import webbrowser

total_breaks = 3
break_time = 60 * 60 * 2
music = ["https://youtu.be/s4EmxvQSpfA?t=1m50s",
        "https://youtu.be/OD3F7J2PeYU?t=10s",
        "https://youtu.be/YQHsXMglC9A?t=2m20s"]

for i in music:
    time.sleep(break_time)
    webbrowser.open(i)
