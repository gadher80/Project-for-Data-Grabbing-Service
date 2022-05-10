import csv
import glob
import pandas as pd
import os
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET
from datetime import datetime
import time

class XmlCofiguration:

    def XmlCongfig(Xml_config_filepath):

        mytree = ET.parse(Xml_config_filepath)
        New_Dict = {}
        for parameter in [parameter.attrib for parameter in mytree.getroot()]:


            for key, value in parameter.items():
                New_Dict[key] = value
        return New_Dict
        #return [parameter.attrib for parameter in mytree.getroot()]

XmlCofiguration.XmlCongfig("Xml files/Configuration file.xml")

class TextConfiguration:

    def Text_Config(Text_config_filepath):

        with open(Text_config_filepath) as Text:
            lines = Text.readlines()

            Parameter_Keywords = ['Catagory', 'Row', 'Column', 'Time', 'When']

            for value in Parameter_Keywords:
                for single_line in lines:
                    if value in single_line:
                        return single_line

class CSV_Durchlesen:

    def __init__(self, path, row, Next_Cycle_In, Stop_Cycle_Time, columns=[]):
        self.path = path
        self.columns = columns
        self.row = row
        self.Next_Cycle_In= Next_Cycle_In
        self.Stop_Cycle_Time= Stop_Cycle_Time

    def csv_file_reading(self):
        df = pd.read_csv(self.path)
        timeout= self.Stop_Cycle_Time
        timeout_start = time.time()
        for row_number in range(self.row + 1):
            Cycle_Start = datetime.now()
            print(time.time()-timeout_start)
            if time.time() < timeout_start + timeout:
                df = df[self.columns].iloc[:row_number]
                time.sleep(self.Next_Cycle_In)
                if os.path.exists('Total_death_of' + ' ' + os.path.basename(self.path)):
                    os.remove('Total_death_of' + ' ' + os.path.basename(self.path))
                    df.to_csv('Total_death_of' + ' ' + os.path.basename(self.path), index=True)
            else:
                break
        return


if __name__=='__main__':
    print(__name__)

    V1 = CSV_Durchlesen("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\csv files\\arizona-history.csv", 24,0.5,8,
                                 ['death', 'hospitalized'])
    V1.csv_file_reading()


class Text_Durchlesen:

    def Text_read(text_file_path):
        global single_line

        with open(text_file_path, "r") as Textfile:
            lines = Textfile.readlines()

        for single_line in lines:
            print(None)

        return single_line

class XML_Durchlesen:

    def XML_read(xml_file_path):
        data = open(xml_file_path).read()
        soup = BeautifulSoup(data, "xml")
        question = soup.find('questionText').string
        ref_ans = soup.find('referenceAnswer').string
        student_answer = soup.find('studentAnswer')
        student_answer_str = student_answer.string
        student_answer_accuracy = student_answer['accuracy']
        print(student_answer_str)
        return student_answer_str


#CSV_Durchlesen.reading_csv("C:\\OPC UA\\OPC UA\\Samples\\alaska-history.csv")