import csv
import math
import numpy as np

from fun_mba import *

msp=50#these are hard coded values for now 
con=70

file='data.csv'

transactions=[]
alle=[]
aller=[]
with open(file, 'r',encoding='utf-8-sig') as csvf:
    csvr=csv.reader(csvf)
    for row in csvr:

        sep= lambda lis: lis.split(sep=',')

        rw=sep(row[1])
        ogrw=[]
        for indx in rw:
            ogrw.append(int(indx))

        x=trans(row[0],ogrw)
        for ele in row[1]:
            try:
                ele=int(ele)
                aller.append(ele)
                if ele not in alle:
                    alle.append(ele)
            except ValueError:
                pass
        alle.sort()
        transactions.append(x)
# ms=math.ceil((msp/100)*len(transactions)) this is the formula for calculation for minimum support , but we are hard coding it to 2 for now
ms=2

# print(f"First transaction: {transactions[0].items} \nall items: {alle} \nmin support: {ms} ")

x = showtime(alle,ms,transactions)#this function is created in the fun_mba library