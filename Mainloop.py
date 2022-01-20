# sourcery skip: for-index-underscore, remove-redundant-pass
import xml.etree.ElementTree as ET
import glob

#import CSV class
from CSV_Extraction_02 import CSV_Durchlesen,XML_Durchlesen, Text_Durchlesen

#Creating a list with all different types of file types
File_ART = ['CSV','Text','XML','MYSQL','EXCEL']

#Calling a configuration file, now in this case it is XML type.
for config_file_path in glob.glob("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\Xml files\*xml"):
    mytree = ET.parse(config_file_path)
    myroot= mytree.getroot()
    #Extracting the data from configuration file
    #for Any_file in glob.glob("C:/Users/har70707/PycharmProjects/IKTS_01/*"):
    for item in myroot.findall('File_config'):
            Config_parameters = item.find('Configuration').attrib
            #here we are getting our all required configuration parameter (now I just took 'Type of file')

            for key,value in Config_parameters.items():
                #now lets check what type of file type it is?
                if value == 'CSV':
                    if value in File_ART:
                        CSV_Instance_01 = CSV_Durchlesen.reading_csv('alaska-history.csv') # calling csv class
                elif value == 'Text':
                    if value in File_ART:
                        Text_Instance_01 = Text_Durchlesen.Text_read("Sample_Example.txt") # calling text class
                elif value == 'XML':
                    if value in File_ART:
                        XML_Instance_01 = XML_Durchlesen.XML_read("XML_Beispiel.xml") # calling xml class
                else:
                    pass