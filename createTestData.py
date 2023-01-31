import os
import pandas as pd

# print(os.path.exists('phishingDetectionphishingDetection/testdataset.csv'))
# print(os.path.dirname(os.path.realpath(__file__)))

df = pd.read_csv('phishingDetection/testdataset.csv')

df = df.reset_index()

lableValues = ['Legitimate', 'Phishing']
Lables = []
for index, row in df.iterrows():
    rowLable = ''
    if (len(row['Title']) > 75):
        import pandas as pd

        df = pd.read_csv('phishingDetection/testdataset.csv')

        df = df.reset_index()

        lableValues = ['Legitimate', 'Suspicious', 'Phishing']
        Lables = []
        for index, row in df.iterrows():
            rowLable = ''
            if (len(row['Title']) > 24):
                rowLable = lableValues[1]
            else:
                rowLable = lableValues[0]
            Lables.append(rowLable)


        df['Lable'] = Lables
        df.drop(columns='index')

        df.to_csv('update.csv', sep=',', encoding='utf-8', index=False)
        import pandas as pd

        df = pd.read_csv('phishingDetection/testdataset.csv')

        df = df.reset_index()

        lableValues = ['Legitimate', 'Suspicious', 'Phishing']
        Lables = []
        for index, row in df.iterrows():
            rowLable = ''
            if (len(row['Title']) > 75):
                rowLable = lableValues[2]
            elif (len(row['Title']) >= 54):
                rowLable = lableValues[1]
            else:
                rowLable = lableValues[0]
            Lables.append(rowLable)


        df['Lable'] = Lables
        df.drop(columns='index')

        df.to_csv('update.csv', sep=',', encoding='utf-8', index=False)
        rowLable = lableValues[2]
    elif (len(row['Title']) >= 54):
            rowLable = lableValues[1]
    else:
        rowLable = lableValues[0]
        Lables.append(rowLable)


        df['Lable'] = Lables
        df.drop(columns='index')

        df.to_csv('update.csv',sep=',', encoding='utf-8', index=False)
