"""
Authour : Hardikkumar Gadher
Location: BITC, Fraunhofer IKTS, Arnstadt
Date: 03.03.2022
Group: OE457
Project: Daten Dienst
"""
import xml.etree.ElementTree as ET

#======================================================================================================
class Global:
    """
    Grabs Global Parameters from configuration file
    """

    def __init__(self, path):

        self.path = path

    def getSourceSections(self):
        """
        Return : Name of all the sources
        ReturnType : List
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        return [(ChildTag.find('SourceSections').text).split(',') for ChildTag in myroot.findall('Global')][0]

    def getExitTriggerSections(self):
        """
        Return : Name of all the Exit Triggers of all sources
        ReturnType : string
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        return [ChildTag.find('ExitTriggerSections').text for ChildTag in myroot.findall('Global')][0]

    def getIdSourceSection(self):
        """
        Return : Name of the source where all IDs of parameters stored
        ReturnType : String
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        return [ChildTag.find('IDSourceSection').text for ChildTag in myroot.findall('Global')][0]
#======================================================================================================
if __name__ == '__main__':
    SourceInstance = Global("Xml files/ConfigExample.xml")
    print(SourceInstance.getSourceSections())



