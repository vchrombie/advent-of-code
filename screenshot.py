import os
import shutil
import mss.tools  # `pip install mss`

from time import sleep
from datetime import datetime

with mss.mss() as sct:
    sleep(1)

    dt = datetime.today()
    day, year = dt.strftime('%d'), dt.strftime('%Y')
    day_png = f"day-{day}.png"

    monitor = {"top": 223, "left": 0, "width": 570, "height": 610}
    sct_img = sct.grab(monitor)
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=day_png)

    shutil.move(day_png, os.path.join(f'day-{day}', day_png))

    # create a gif using ImageMagick `brew install imagemagick`
    os.system(f"convert -delay 50 */*.png {year}.gif")
