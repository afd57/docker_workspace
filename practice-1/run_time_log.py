import os
import time
from datetime import datetime

with open("log-1.txt",'w') as file:
    for key, val in os.environ.items():
        print(f"{key}: {val}")
        file.write(f"{key}: {val}\n")

    while(True):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        file.write(f"CURRENT TIME: {current_time}\n")
        file.flush()
        time.sleep(10)
