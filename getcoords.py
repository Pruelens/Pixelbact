

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import random
import xlrd3
import os

script_path = os.path.realpath(__file__)
try:
    input_sheet=input("Enter  sheet name of excel colorexcel.xlsx with pixel art: ")
    df = pd.read_excel(script_path[:-7]+'colorexcel.xlsx', sheet_name=input_sheet, index_col=0)
    print('Design successfully loaded')

except:
    print('incorrect sheet name, check sheet name and whether colorexcel.xlsx is in same directory as this python script ')
    exit()
input_name = input("Enter the name of your design:")

columnslist=df.columns.values.tolist()
row_list = df.index.tolist()

list(df)
df  = df.iloc[: , :28]

C1_list=[]
C2_list=[]
C3_list=[]
C4_list=[]
C5_list=[]
C6_list=[]
C7_list=[]
C8_list=[]

for rows,row_index in zip(df.iterrows(),row_list):
    for col,col_index in zip(rows[1],columnslist):
        coord=str(row_index)+''+str(col_index)
        if col==1:
            C1_list.append(coord)
        if col == 2:
            C2_list.append(coord)
        if col == 3:
            C3_list.append(coord)
        if col == 4:
            C4_list.append(coord)
        if col==5:
            C5_list.append(coord)
        if col == 6:
            C6_list.append(coord)
        if col==7:
            C7_list.append(coord)
        if col == 8:
            C8_list.append(coord)






f = open('pixelbact_OT2.py','r+')
lines = f.readlines() # read old content
f.close()
seed=random.randrange(10000)
f = open('Generated_pixelbact_OT2_'+input_name+'.py',"w+")

f.seek(0) # go back to the beginning of the file
f.write('Color1_list='+str(C1_list)+ '\n')
f.write('Color2_list='+str(C2_list)+ '\n')
f.write('Color3_list='+str(C3_list)+ '\n')
f.write('Color4_list='+str(C4_list)+ '\n')
f.write('Color5_list='+str(C5_list)+ '\n')
f.write('Color6_list='+str(C6_list)+ '\n')
f.write('Color7_list='+str(C7_list)+ '\n')
f.write('Color8_list='+str(C8_list)+ '\n')
f.write('\n')
for line in lines: # write old content after new
    f.write(line)
f.close()




