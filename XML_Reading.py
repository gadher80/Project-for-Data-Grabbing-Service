import glob
from bs4 import BeautifulSoup
import os

class XML_Durchlesen:

    def XML_read(file_path_xml):
            data = open(file_path_xml).read()
            soup = BeautifulSoup(data, "xml")
            question = soup.find('questionText').string
            ref_ans = soup.find('referenceAnswer').string
            student_answer = soup.find('studentAnswer')
            student_answer_str = student_answer.string
            student_answer_accuracy = student_answer['accuracy']
            print(student_answer_str)
            return student_answer_str


# def XML_Durchlesen(files):
#     files = glob.glob("C:\OPC UA\OPC UA\Samples\XML_Beispiel.xml")
#     for file in files:
#         data = open(file).read()
#         soup = BeautifulSoup(data, "xml")
#         question = soup.find('questionText').string
#         ref_ans = soup.find('referenceAnswer').string
#         student_answer = soup.find('studentAnswer')
#         student_answer_str = student_answer.string
#         student_answer_accuracy = student_answer['accuracy']
#     return student_answer_str

#XML_Durchlesen.XML_read("C:\OPC UA\OPC UA\Samples\XML_Beispiel.xml")