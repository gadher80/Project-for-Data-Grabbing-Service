#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

import csv
import glob

#Beatifulsoup and xml etree will be needed to read xml version of file
from bs4 import BeautifulSoup
from datetime import datetime

import xml.etree.ElementTree as ET
from datetime import datetime
import time

class XmlImport:

    # now we are now initializing xml class
    # Ziel: To grab our desired config paramaters from raw xml file

    #here I have grabbed only simple pre- defined parameters like here : questionText, referenceAnswer, studentAnswer, accuracy
    # We can also generate self method to grab only our desired parameters.
    def __init__(self,xml_file_path):

        self.xml_file_path = xml_file_path

    def XmlRead(self):

        xmlData = open(self.xml_file_path).read()

        soup = BeautifulSoup(xmlData, "xml")

        question = soup.find('questionText').string

        ref_ans = soup.find('referenceAnswer').string

        student_answer = soup.find('studentAnswer')

        student_answer_str = student_answer.string

        student_answer_accuracy = student_answer['accuracy']

        return [question, ref_ans, student_answer_str,student_answer_accuracy]

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
