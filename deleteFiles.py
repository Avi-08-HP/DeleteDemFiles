import os
import time

#folder to clear from
dir_path = 'path of directory to clean'
#No of days before which the files are to be deleted
limit_days = 30

treshold = time.time() 
entries = os.listdir(dir_path)
for dir in entries:
    creation_time = os.stat(os.path.join(dir_path,dir)).st_ctime
    if creation_time < treshold:
        print(f"{dir} is created on {time.ctime(creation_time)} and will be deleted. Also bruh, please, cleaning your folders doesn't take that much time.")