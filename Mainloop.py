import xml.etree.ElementTree as ET

#import CSV class
from CSV_Extraction_02 import CSV_Durchlesen

#import XML class
from XML_Reading import XML_Durchlesen

#import XML class
from Text_Extraction import Text_Durchlesen

#Creating a list with all different types of file types
File_ART = ['CSV','TEXT','XML','MYSQL','EXCEL']

#Calling a configuration file, now in this case it is XML type.
mytree = ET.parse('XML_Datengrabber.xml')
myroot= mytree.getroot()

#Extracting the data from configuration file
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
