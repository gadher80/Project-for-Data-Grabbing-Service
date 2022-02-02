import csv
import time
from datetime import datetime
from Upload import writeRows
import cv2
import keyboard


def getLength(path):

    with open(path,'r') as READ:
        csvreader = csv.reader(READ)
        return len(list(csvreader))

while True:
    NumberOfRowsBefore = getLength('New_Arizona.csv')
    print(NumberOfRowsBefore)
    time.sleep(1)
    NumberOfRowsAfter = getLength('New_Arizona.csv')
    print(NumberOfRowsAfter)
    if NumberOfRowsAfter != NumberOfRowsBefore:
        if keyboard.is_pressed('q'):
            print('q is pressed')
        else:
            with open('New_Arizona.csv') as READ:
                csvreader = csv.reader(READ)
                print(list(csvreader)[NumberOfRowsBefore:])
    else:
        print('No New Rows added')
        break
