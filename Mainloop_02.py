# sourcery skip: for-index-underscore, remove-redundant-pass
import os.path
import xml.etree.ElementTree as ET
import glob
import time

#import CSV class
from CSV_Extraction_02 import CSV_Durchlesen,XML_Durchlesen, Text_Durchlesen, XmlCofiguration, TextConfiguration


#Calling a configuration class file, now in this case it is XML type.

Reading = XmlCofiguration.XmlCongfig('Xml files/Configuration file.xml')

# Extracting the data from configuration file
# for Any_file in glob.glob("C:/Users/har70707/PycharmProjects/IKTS_01/*"):
    # here we are getting our all required configuration parameter (now I just took 'Type of file')

for key, value in Reading.items():
    # now lets check what type of file type it is?

    if value == 'CSV':
        # Getting each file from the folder of csv files and extracting our data
        CSV_Instance_01 = CSV_Durchlesen("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\csv files\\arizona-history.csv", 24,0.5,10, ['death','hospitalized'])
        # calling csv class
        CSV_Instance_01.csv_file_reading()

    if  value == 'Text':

        # Getting each file from the folder of text files and extracting our data

        for text_grabber in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Text files\*"):
            Text_Instance_01 = Text_Durchlesen.Text_read(text_grabber)  # calling text class

    if value == 'XML':

        # Getting each file from the folder of xml files and extracting our data

        for xml_grabber in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Xml input files\*"):
            XML_Instance_01 = XML_Durchlesen.XML_read(xml_grabber)  # calling xml class

    else:
        pass