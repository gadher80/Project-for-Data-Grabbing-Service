class Text_Durchlesen:

    def Text_read(path):
        with open(path, "r") as f:
            lines = f.readlines()
        for single_line in lines:
            print(single_line)
        return single_line

#Text_Durchlesen.Text_read("C:\OPC UA\OPC UA\Samples\Sample_Example.txt")





