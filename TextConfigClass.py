#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =

class TextConfiguration:

    # now we are now initializing xml configuration class
    # Goal: to grab configuration parameters from text file

    def __init__(self,Text_config_filepath):

        self.Text_config_filepath = Text_config_filepath

    def TextConfig(self):

        with open(self.Text_config_filepath) as Text:
            lines = Text.readlines()

            parameterKeywords = ['Catagory', 'Row', 'Column', 'Time', 'When'] # we want these parameters from config file

            for value in parameterKeywords:

                for singleLine in lines:

                    if value in singleLine:

                        return singleLine

#== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
