#This is our main loop, using this we can grab our desired data

#importing needed pacakges

import os.path
import xml.etree.ElementTree as ET
import glob
import time

#importing all importer class like confi classes, csv class, xml class, text class
from DatenGrabberClasses import CSV_Durchlesen,XML_Durchlesen, Text_Durchlesen, XmlCofiguration, TextConfiguration


#Calling a configuration class file, now in this case it is XML type.
#creating Instance for getting config paramaters
Reading = XmlCofiguration.XmlCongfig('Xml files/Configuration file.xml')


# Extracting the data from configuration file

for key, value in Reading.items():
    # now lets check what type of file type it is?

    if value == 'CSV':

        # calling csv class and creating its instance

        CSV_Instance_01 = CSV_Durchlesen("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\csv files\\arizona-history.csv",
                                         24,0.5,10, ['death','hospitalized'])

        CSV_Instance_01.CsvRead()

    if  value == 'Text':

        # Getting each file from the folder of text files and extracting our data

        for text_grabber in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Text files\*"):

            # calling text class
            Text_Instance_01 = Text_Durchlesen.TextRead(text_grabber)

    if value == 'XML':

        # Getting each file from the folder of xml files and extracting our data

        for xml_grabber in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Xml input files\*"):

            # calling xml class
            XML_Instance_01 = XML_Durchlesen.XmlRead(xml_grabber)

    else:
        pass