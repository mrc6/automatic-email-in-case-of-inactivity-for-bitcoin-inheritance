import time
from datetime import datetime

timestr = time.strftime("%Y%m%d-%H%M%S")

with open('lastbeat.txt', 'w+') as f:
    f.write(timestr)
    f.close()

input_key = input('Your hit was save successfully. Press any key to exit!')