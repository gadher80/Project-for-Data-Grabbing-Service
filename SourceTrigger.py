"""
Authour : Hardikkumar Gadher
Location: BITC, Fraunhofer IKTS, Arnstadt
Date: 03.03.2022
Group: OE457
Project: Daten Dienst
"""
from Sources import *
#======================================================================================================
class SourceTrigger(Sources):
    """
    Grabs Different Source Trigger Parameters from configuration file
    """
    def __init__(self,path):
        super().__init__(path)

    def getTriggers(self):
        """
        Return : Trigger Parameters for all sources
        ReturnType : Dictionary
        """
        mytree = ET.parse(self.path)
        myroot = mytree.getroot()

        triggerdict = {}
        Trigger = Sources(self.path)
        triggerValues = Trigger.getSource()
        triggers = {}

        for key, value in triggerValues.items():
            for subKey, subValue in value.items():
                if subKey == 'TriggerSection':
                    triggers[key] = subValue

        for trigger, triggerText in triggers.items():
            for sourcePara in myroot.find(triggerText):
                triggerdict[triggerText] = {child.tag: child.text for child in myroot.find(triggerText)}

        return triggerdict
#======================================================================================================
if __name__ == "__main__":
    SourceExample = SourceTrigger("Xml files/ConfigExample.xml")
    print(SourceExample.getTriggers())

