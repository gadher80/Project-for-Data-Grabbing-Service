"""
Authour : Hardikkumar Gadher
Location: BITC, Fraunhofer IKTS, Arnstadt
Date: 03.03.2022
Group: OE457
Project: Daten Dienst
"""
from IDSource import *
#======================================================================================================
class Sources(IDSource):
    """
    Grabs Different Source Parameters from configuration file
    """
    def __init__(self,path):
        super().__init__(path)

    def getSource(self):
        """
        Return : All sources
        ReturnType : Dictionary
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        sourceAll = {}
        Sources = Global(self.path)

        for sourceTag in Sources.getSourceSections():

            for sourcePara in myroot.find(sourceTag):
                sourceAll[sourceTag] = {child.tag : child.text for child in myroot.find(sourceTag)}

        return sourceAll

    def getPara(self, any):
        """
        Return : Any desired parameter from all sources
        ReturnType : Dictionary
        """
        self.any = any

        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        catagoryDict = {}
        Sources = Global(self.path)

        for sourceTag in Sources.getSourceSections():
                for childTag in myroot.findall(sourceTag):
                    if childTag.find(self.any) is None:
                        catagoryDict[sourceTag] = None
                    else:
                        catagoryDict[sourceTag] = childTag.find(self.any).text

        return catagoryDict

    def getSubtype(self):
        """
        Return : Subtype of all the sources
        ReturnType : Dictionary
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        subtypeDict = {}
        Sources = Global(self.path)

        for sourceTag in Sources.getSourceSections():
            for chilTag in myroot.findall(sourceTag):
                subtypeDict[sourceTag] = chilTag.find('SubType').text

        return subtypeDict

    def getAddress(self):
        """
        Return : Addresses of all the sources
        ReturnType : Dictionary
        """
        global chilTag
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        addressDict = {}
        Sources = Global(self.path)

        for sourceTag in Sources.getSourceSections():
            for chilTag in myroot.findall(sourceTag):
                addressDict[sourceTag] = eval(chilTag.find('Address').text)

        return addressDict

    def getType(self):
        """
        Return : types of all the sources
        ReturnType : Dictionary
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        typeDict = {}
        Sources = Global(self.path)

        for sourceTag in Sources.getSourceSections():
            for chilTag in myroot.findall(sourceTag):
                typeDict[sourceTag] = chilTag.find('Type').text

        return typeDict

    def getCategory(self):
        """
        Return : category of all the sources
        ReturnType : Dictionary
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        categoryDict = {}
        Sources = Global(self.path)

        for sourceTag in Sources.getSourceSections():
            for chilTag in myroot.findall(sourceTag):
                categoryDict[sourceTag] = chilTag.find('Category').text

        return categoryDict
#======================================================================================================
if __name__ == "__main__":
    SourceExample = Sources("Xml files/ConfigExample.xml")
    print(SourceExample.getPara('Columns'))

