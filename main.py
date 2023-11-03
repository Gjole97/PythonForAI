import pandas as pd
pd.set_option('display.max_columns', 500)
data = pd.read_csv('excel-comp-data.csv')

for index, row in data.iterrows():
    print('Name:', row['name'], 'City:', row['city'], 'Income:', row['Jan']+row['Feb']+row["Mar"])
    print("Bojan")
    print('Gjorgji')
    print('Viktor')
    print('Elena')
