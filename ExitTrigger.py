"""
Authour : Hardikkumar Gadher
Location: BITC, Fraunhofer IKTS, Arnstadt
Date: 03.03.2022
Group: OE457
Project: Daten Dienst
"""
from IDSource import *
#======================================================================================================
class ExitTrigger(IDSource):
    """
    Grabs Trigger Parameters from configuration file
    """
    def __init__(self, path):
        super().__init__(path)

    def getTrigger(self):
        """
        Return : Trigger Parameters of whole Data Service
        ReturnType : String
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        Trigger = Global(self.path)

        return {
            sourcePara.tag: sourcePara.text
            for sourcePara in myroot.find(Trigger.getExitTriggerSections())
        }
#======================================================================================================
if __name__ == "__main__":
    SourceExample = ExitTrigger("Xml files/ConfigExample.xml")
    print(SourceExample.getTrigger())
