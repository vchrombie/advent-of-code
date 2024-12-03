import os
import shutil
import mss.tools

from time import sleep
from datetime import datetime

with mss.mss() as sct:
    sleep(1)
    monitor = {"top": 200, "left": 0, "width": 570, "height": 610}
    dt = datetime.today()
    day, year = dt.strftime('%d'), dt.strftime('%Y')
    sct_img = sct.grab(monitor)

    year_png = "{}.png".format(year)
    day_png = "day-{}.png".format(day)

    mss.tools.to_png(sct_img.rgb, sct_img.size, output=year_png)
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=day_png)

    shutil.move(day_png, os.path.join(f'day-{day}', day_png))
