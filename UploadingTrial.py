import csv
import time
from datetime import datetime



# def CsvInProcess(path):
#     with open(path, newline='') as csvFile:
#         csvreader = csv.reader(csvFile)
#         #print(list(csvreader))
#
#         # header = []
#         # header = next(csvreader)
#         # print(header)
#
#         # with open('New_Arizona.csv', 'w') as addHeader:
#         #     Write = csv.writer(addHeader, delimiter=',')
#         #     Write.writerow(header)
#
#         timeout = 10  # [seconds]
#         timeout_start = time.time()
#         # print(time.time())
#         Readinglist = list(csvreader)
#         for row in Readinglist:
#             with open('New_Arizona.csv', 'a', newline='') as writeToCsv:
#                 csvreader = csv.reader(writeToCsv)
#                 writer = csv.writer(writeToCsv, delimiter=',')
#                 if time.time() < timeout_start + timeout:
#                     writer.writerow(row)
#                     Readinglist.remove(row)
#                     time.sleep(0.5)
#
#         return
#
TotalRows = []
AddedRows = []
timeout = 20  # [seconds]
timeout_start = time.time()

with open('New_Arizona.csv') as READ:
    reader = csv.reader(READ)
    length01 = len(list(reader))
    TotalRows.append(length01)
    if len(AddedRows) != 0:
        if len(TotalRows) > 1:
            print(AddedRows[TotalRows[0]:TotalRows[1] + 1])
            TotalRows = []
        else:
            print('It is just a start')
    else:
        print('There are no rows')
    with open('csv files/CsvProb.csv', newline='') as csvFile:
        csvreader = csv.reader(csvFile)
        # print(list(csvreader))

        # header = []
        # header = next(csvreader)
        # print(header)

        # with open('New_Arizona.csv', 'w') as addHeader:
        #     Write = csv.writer(addHeader, delimiter=',')
        #     Write.writerow(header)

        timeout = 20  # [seconds]
        timeout_start = time.time()
        # print(time.time())
        Readinglist = list(csvreader)
        for row in Readinglist:
            with open('New_Arizona.csv', 'a', newline='') as writeToCsv:
                csvreader = csv.reader(writeToCsv)
                writer = csv.writer(writeToCsv, delimiter=',')
                if time.time() < timeout_start + timeout:
                    writer.writerow(row)
                    Readinglist.remove(row)
                    AddedRows.append(row)
                    time.sleep(1)



        #
#length02 = len(list(reader))
        # print(length02)

#CsvInProcess('csv files/arizona-history.csv')



# def NewRows(path2,path):
#
#     with open(path2, 'r', newline='') as readDynamicCsv:
#         csvreader = csv.reader(readDynamicCsv)
#         Object2 = CsvInProcess(path)
#         print(Object2)
#         if Object2 < len(list(csvreader)):
#             print('We have new rows')
#         else:
#             print('No new rows')
#
#     return


#CsvInProcess('csv files/arizona-history.csv')
#NewRows('csv files/arizona-history.csv','New_Arizona.csv')