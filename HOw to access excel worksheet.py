import pandas as pd

#To read excel file.
df=pd.read_excel('C:\\dataset\\Customer_dataset.xlsx')

#To print the file
print(df)

#To print the length of file
print(len(df))

#To print the shape of file i.e rows and columns
print(df.shape)

#To print the first five records
print(df.head())

#To print the count of unique values
print(df.value_counts())

#Separation line
print('***********************************************************')

#To print the row in which Customer name is John
print(df[df['Customer_name']=='John'])

# To print the row in which state is SA
print(df[df['State']=='SA'])

# To print the row in which Country is NYC
print(df[df['Country']=='NYC'])
