import csv
import time
from datetime import datetime

timeout = 100  # [seconds]
timeout_start = time.time()


def writeRows(path):

    with open(path, newline='') as csvFile:
        csvreader = csv.reader(csvFile)

        for row in csvreader:

            with open('New_Arizona.csv', 'a', newline='') as writeToCsv:
                csvreader = csv.reader(writeToCsv)
                if time.time() < timeout_start + timeout :
                    writer = csv.writer(writeToCsv, delimiter=',')
                    writer.writerow(row)
                    time.sleep(0.5)
                else:
                    print('Time Out')
                    break
    return

if __name__ == '__main__':

    writeRows('csv files/CsvProb.csv')

