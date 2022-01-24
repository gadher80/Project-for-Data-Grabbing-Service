# sourcery skip: for-index-underscore, remove-redundant-pass
import os.path
import xml.etree.ElementTree as ET
import glob
import time

#import CSV class
from CSV_Extraction_02 import CSV_Durchlesen,XML_Durchlesen, Text_Durchlesen

#Calling a configuration file, now in this case it is XML type.
for config_file_path in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Xml files\*xml"):
    print(f'Jetzt nehme ich Konfiguration {os.path.basename(config_file_path)} und untersuche auf der Konfiguration Parameter')

    mytree = ET.parse(config_file_path)
    myroot= mytree.getroot()

    #Extracting the data from configuration file
    #for Any_file in glob.glob("C:/Users/har70707/PycharmProjects/IKTS_01/*"):
    for item in myroot.findall('File_config'):
            Config_parameters = item.find('Configuration').attrib
            print(Config_parameters)
            #here we are getting our all required configuration parameter (now I just took 'Type of file')

            for key,value in Config_parameters.items():
                #now lets check what type of file type it is?
                if value == 'CSV':

                    #Getting each file from the folder of csv files and extracting our data

                    for csv_grabber in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\csv files\*"):
                        CSV_Instance_01 = CSV_Durchlesen.reading_csv(csv_grabber) # calling csv class

                elif value == 'Text':

                    #Getting each file from the folder of text files and extracting our data

                    for text_grabber in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Text files\*"):
                        Text_Instance_01 = Text_Durchlesen.Text_read(text_grabber) # calling text class

                elif value == 'XML':

                    #Getting each file from the folder of xml files and extracting our data

                    for xml_grabber in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Xml input files\*"):
                        XML_Instance_01 = XML_Durchlesen.XML_read(xml_grabber) # calling xml class

                else:
                    pass