"""This Class is an importer of data, what it does ?
It grabbes the data from RAW Csv file and import it to new Csv file"""

"""I created this because, in real time we will get our data automatically from machines, 
now we dont have our real data from machines, so but now for temporary base, I had to do this for getting results"""


#import necessary packages

import csv
import time
from datetime import datetime

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

class DataImporter:

    #Goal: This class will write rows to new csv file from old csv file

    def __init__(self,NewCsvPath):

        self.NewCsvPath = NewCsvPath

    def writeRows(self):

        #defining method : Grab a row every x seconds for total y seconds

        #this is our real time Eg. 02.02.2022 18.39.45z
        timeout_start = time.time()

        #opening old csv file to read
        with open('csv files/CsvProb.csv', newline='') as csvFile:
            csvreader = csv.reader(csvFile)

            #Iterate over all rows
            for row in csvreader:

                #now opening new csv file to write from old csv file
                with open(self.NewCsvPath, 'a', newline='') as writeToCsv:
                    csvreader = csv.reader(writeToCsv)

                    #Only write if time is in period of our trigger time
                    #For Example we say we want to keep adding rows for 500 secs,
                    #so after 100 secs this won't work, and will break a loop

                    if time.time() < timeout_start + 500:  # 100 is timeout time so (current time + time out time) exceeds time limit then, break the loop

                        #wirting a row
                        writer = csv.writer(writeToCsv, delimiter=',')
                        writer.writerow(row)

                        #here loop will stop for given sleep time and runs again
                        time.sleep(0.5)
                        
                    else:

                        #if time is more than trigger time, just break the loop
                        print('Time Out')
                        break
        return

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

if __name__ == '__main__':

    Object = DataImporter('New_Arizona.csv')
    Object.writeRows()
