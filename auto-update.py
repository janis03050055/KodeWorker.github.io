import os
import datetime

if __name__ == '__main__':
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.system('git add . & git commit -m "%s update" & git push origin master' %date)