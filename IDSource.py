"""
Authour : Hardikkumar Gadher
Location: BITC, Fraunhofer IKTS, Arnstadt
Date: 03.03.2022
Group: OE457
Project: Daten Dienst
"""
from Global import *
#======================================================================================================
class IDSource(Global):
    """
    Grabs Parameters of particular source where all IDs are stored
    """
    def __init__(self, path):
        super().__init__(path)

    def getType(self):
        """
        Return : Type of ID Source
        ReturnType : String
        """
        global getType
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        for ChildTag in myroot.findall(Global.getIdSourceSection(self)):
            getType = ChildTag.find('Type').text

        return getType

    def address(self):
        """
        Return : Address of ID Source
        ReturnType : String
        """
        global address
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        for ChildTag in myroot.findall(Global.getIdSourceSection(self)):
            address = ChildTag.find('Address').text

        return address
#======================================================================================================
if __name__ == '__main__':
    SourceInstance = IDSource("Xml files/ConfigExample.xml")
    print(SourceInstance.address())