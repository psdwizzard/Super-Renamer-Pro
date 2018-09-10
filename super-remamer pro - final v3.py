import os
import csv
import shutil
#from pathlib import Path

start = raw_input("Where are your current file?")

if (os.path.isdir(start + '/save')):
    with open(start + '/' +'old-names-new-names.csv','rt') as csvfile:
        timeReader = csv.reader(csvfile, delimiter = ',')
        i = 0 
        for row in timeReader:
            if i > 0:
                start_loc = row[1]
                save_loc = row[0]
                shutil.copyfile(start +'/{}'.format(start_loc), start +'/save/{}'.format(save_loc))
            i+=1
else:
    os.mkdir(start + '/' +"save")
    with open(start + '/' +'old-names-new-names.csv','rt') as csvfile:
        timeReader = csv.reader(csvfile, delimiter = ',')
        i = 0 
        for row in timeReader:
            if i > 0:
                start_loc = row[1]
                save_loc = row[0]
                shutil.copyfile(start +'/{}'.format(start_loc), start +'/save/{}'.format(save_loc))
            i+=1
