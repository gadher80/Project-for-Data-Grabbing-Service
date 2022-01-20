import csv
import glob
import pandas as pd
from datetime import datetime

class CSV_Durchlesen:

    def reading_csv(Path):
        df1 = pd.DataFrame()
        df = pd.read_csv(Path)
        state_name = df.iloc[1]['state']
        df1['dates'] = df['date']
        df1[state_name] = df['death']
        df1 = df1.rename(columns={'dates': 'Date', 'AK': 'Alaska', 'AZ': 'Arizona', 'CL': 'California', 'CT': 'Connecticut',
                                  'MA': 'Massechusetts'})
        df1 = df1.dropna(axis=0, how='any')
        df1.to_csv('Total_death.csv', index=False)
        return df1


#CSV_Durchlesen.reading_csv("C:\\OPC UA\\OPC UA\\Samples\\alaska-history.csv")