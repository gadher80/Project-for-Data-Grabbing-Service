import os.path
import xml.etree.ElementTree as ET
import glob
import time

#importing all importer class like confi classes, csv class, xml class, text class
import CsvImporter
from CsvImporter import CheckNewRows
from XmlImporter import XmlImport
from TextImpoter import TextImpot
from XmlConfigClass import XmlCofiguration
from TextConfigClass import TextConfiguration

#Calling a configuration class file, now in this case it is XML type.
#creating Instance for getting config parameters

# Extracting the data from configuration file
XmlConfigRead = XmlCofiguration('Xml files/Configuration file.xml')
ConfigDict= XmlConfigRead.XmlConfig()

timeout_start =time.time()

# now lets check what type of file type it is?

#now we will detect type of file from config parameter
while True:

    #first check for if it is csv
    if ConfigDict['category'] == 'CSV':

        # start the loop if time is still permitted before triggered
        while time.time() < timeout_start + int(ConfigDict['Trigger']):

            # get the length of csv rows at T = 0 sec

            NumberOfRowsBefore = CheckNewRows(ConfigDict['address'])
            RowsAtTime01 = NumberOfRowsBefore.getLength()
            print(RowsAtTime01)

            # check every( eg. 10 sec) that if there are any changes
            time.sleep(int(ConfigDict['TimePeriod']))

            # get the length of csv rows at T = (0 + 10 )seconds
            NumberOfRowsAfter = CheckNewRows(ConfigDict['address'])
            RowsAtTime02 = NumberOfRowsAfter.getLength()
            print(RowsAtTime02)

            ChangeInRows = RowsAtTime02 - RowsAtTime01

            # if changes then, grab only new rows
            if ChangeInRows > 0:

                getChange = CheckNewRows(ConfigDict['address'])
                getChange.ReadCsv(RowsAtTime01, eval(ConfigDict['Column']))

            else:

                print('No new rows were added')

        print('\n\nTime is triggered just now')
        break

    if ConfigDict['category'] == 'Text':

        # calling text class
        Text_Instance_01 = TextImpot(ConfigDict['address'])
        Text_Instance_01.TextRead()
        break

    if ConfigDict['category'] == 'XML':

        # calling xml class
        XML_Instance_01 = XmlImport(ConfigDict['address'])
        XML_Instance_01.XmlRead()
        break
