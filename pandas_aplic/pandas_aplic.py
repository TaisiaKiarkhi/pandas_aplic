
import pandas as pd


data = {'Name': ['Ola', 'Mona', 'Kim'],
        'Age': [23, 45, 19],
         
    }

data_frame  =pd.DataFrame(data)

# data_frame = pd.read_csv('C:/Users/Taisa/Desktop/CSV_files/data.csv', sep = '\t') #enter a file path to read csv file
print(data_frame)
print(data_frame['Name'])
print(data_frame['Age'].max())

print(data_frame.describe())

above_23 = data_frame['Age'] > 23
print(above_23)
print(data_frame[above_23])
print(array_)