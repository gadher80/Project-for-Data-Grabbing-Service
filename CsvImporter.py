"""This module introduces a class which checks if there are new rows added or not,
if yes then then it will grab those newely added rows and will give a list of them"""

"""Here we would need just our new csv path """
"""Part01 : Check Length of New csv file"""
"""Part02: If there are any changes, grab the changes"""

#Importing necessary packages
import csv
import time
from datetime import datetime
import pandas as pd

#importing  a class which is continuously adding new data
from UploadingDataTemp import DataImporter

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =


class CheckNewRows:

    #Goal :  This class has a method which reads new csv file and give us newly added rows
    #This class also inherits parent class

    def __init__(self,NewCsvPath):

        self.NewCsvPath = NewCsvPath


    def getLength(self):

        #This method counts number of rows in csv
        df = pd.read_csv(self.NewCsvPath)
        return len(df.index)


        # #checking a length(number of rows) of new csv file
        # with open(self.NewCsvPath,'r') as READ:
        #     csvreader = csv.reader(READ)
        #     return len(list(csvreader))

    def ReadCsv(self, RowDifference, ColumnNames = []):

        #This method grabs the data if there is any change

        self.ColumnNames = ColumnNames
        self.RowDifference = RowDifference


        df = pd.read_csv(self.NewCsvPath, usecols=self.ColumnNames)
        df = df.iloc[self.RowDifference : ]
        print(df)

        #returning news rows as a list so we can use them later on
        return df.values.tolist()

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

if __name__ == '__main__':

    Object = CheckNewRows('New_Arizona.csv')
    Object.ReadCsv(1, ['death', 'deathConfirmed'])

