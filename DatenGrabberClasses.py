
"""
Created on Thu 26-01-2022  07:15:17 2020

@author: Hardikkumar Gadher
@date: 26-01-2022
@description: Program to avail different data services as per requirement
"""

#importing all needed packages

import csv
import glob
import pandas as pd
import os

#Beatifulsoup and xml etree will be needed to read xml version of file
from bs4 import BeautifulSoup
from datetime import datetime

import xml.etree.ElementTree as ET
from datetime import datetime
import time

""" This program will able to get the data as per requirement,
and push them to our desired output file versions, this service we call it different 'Data Services'.

Every particular data service would require configuration file,
where whole ideaology of impoter class can be understood,
either it would be xml, csv or text or any other one.

from configuration file, one can know type of raw file(csv, xml, text), what data from that file we are looking for, 
how often data should be grabbed, how long service should run etc.

"""

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

#Therefore, now we are now initializing xml configuration class
# Ziel:  To grab configuration parameters from xml file

class XmlCofiguration:

    def XmlCongfig(Xml_config_filepath): #definig parsing/ reading method from xml

        myTree = ET.parse(Xml_config_filepath)

        configParameter = {} #calling empty dictionary to store all configuration parameters

        for parameter in [parameter.attrib for parameter in myTree.getroot()]:

            for key, value in parameter.items():
                configParameter[key] = value

        return configParameter # this method will give us a dictionary where all config parameters are stored

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

#Trial for above defined class

if __name__=='__main__':

    xml_trialInstance = XmlCofiguration()

    xml_trialInstance.XmlCongfig("Xml files/Configuration file.xml")

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

#now we are now initializing xml configuration class
# Ziel: to grab configuration parameters from text file

class TextConfiguration:

    def Text_Config(Text_config_filepath):

        with open(Text_config_filepath) as Text:
            lines = Text.readlines()

            parameterKeywords = ['Catagory', 'Row', 'Column', 'Time', 'When'] # we want these parameters from config file

            for value in parameterKeywords:

                for singleLine in lines:

                    if value in singleLine:

                        return singleLine

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

#now we are now initializing csv class
# Ziel: To grab our desired config paramaters from raw csv file

class CSV_Durchlesen:

    def __init__(self, path, row, Next_Cycle_In, triggerTime, columns=[]): # we need these parameters from our raw file

        self.path = path
        self.columns = columns
        self.row = row
        self.NextCycle_In= Next_Cycle_In
        self.triggerTime= triggerTime

    def CsvRead(self):

        df = pd.read_csv(self.path)

        # at this time our loop will break and stop
        timeout= self.triggerTime

        # at this loop is starting
        timeoutStart = time.time()

        for rowNumber in range(self.row + 1):

            Cycle_Start = datetime.now()

            print(time.time()-timeoutStart)

            if time.time() < timeoutStart + timeout:

                df = df[self.columns].iloc[:rowNumber]

                # this much often next row will be added (z.B Every 5 seconds new row would be grabbed)
                time.sleep(self.Next_Cycle_In)

                # if new created csv file is already existed then delete it
                if os.path.exists('Total_death_of' + ' ' + os.path.basename(self.path)):

                    os.remove('Total_death_of' + ' ' + os.path.basename(self.path))

                    # creating new csv output file to store grabbed data
                    df.to_csv('Total_death_of' + ' ' + os.path.basename(self.path), index=True)
            else:
                break
        return

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

#Trial for above defined class

if __name__=='__main__':

    csvTrial_Instance = CSV_Durchlesen("C:\\Users\\har70707\\PycharmProjects\\IKTS_01\\csv files\\arizona-history.csv", 24, 0.5, 8,
                                       ['death', 'hospitalized'])

    csvTrial_Instance.CsvRead()

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

#now we are now initializing csv class
#  Ziel: To grab our desired config paramaters from raw text file

class Text_Durchlesen:

    def TextRead(text_file_path):
        global single_line

        with open(text_file_path, "r") as Textfile:
            lines = Textfile.readlines()

        for single_line in lines:
            print(None)

        return single_line

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

#now we are now initializing xml class
# Ziel: To grab our desired config paramaters from raw xml file

class XML_Durchlesen:

    #here I have grabbed only simple pre- defined parameters like here : questionText, referenceAnswer, studentAnswer, accuracy
    # We can also generate self method to grab only our desired parameters.

    def XmlRead(xml_file_path):

        xmlData = open(xml_file_path).read()

        soup = BeautifulSoup(xmlData, "xml")

        question = soup.find('questionText').string

        ref_ans = soup.find('referenceAnswer').string

        student_answer = soup.find('studentAnswer')

        student_answer_str = student_answer.string

        student_answer_accuracy = student_answer['accuracy']

        return student_answer_str

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

