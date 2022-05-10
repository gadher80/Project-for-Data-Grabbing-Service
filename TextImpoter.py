#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

class TextImpot:
    # now we are now initializing csv class
    #  Ziel: To grab our desired config paramaters from raw text file
    def __init__(self,text_file_path):

        self.text_file_path = text_file_path

    def TextRead(self):


        with open(self.text_file_path, "r") as Textfile:
            lines = Textfile.readlines()

        return list(lines)

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
