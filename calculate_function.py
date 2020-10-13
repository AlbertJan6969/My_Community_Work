import matplotlib.pyplot as plt
import random
from xlrd import open_workbook
import math
x_data = []
y_data = []
fre=[]
specialFre=[]
x_volte = []
temp = []
name=[]
wb = open_workbook('data.xlsx.')

for s in wb.sheets():
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        name.append(values[0])
        x_data.append(values[1])
        y_data.append(values[2])
        specialFre.append(values[4])

for q in range (0,48):
    NAME=name[q]
    XNAME=NAME+"X"
    YNAME = NAME + "Y"
    XNAMEd=x_data[q]
    YNAMEd=y_data[q]
    ANAME=NAME+"A"
    print(ANAME,"=",specialFre[q])
    # print(XNAME,"=",XNAMEd)
    # print(YNAME,"=",YNAMEd)

A2X = 30.07
A2Y = 23.44
O1X = 7.24
O1Y = 23.52
O2X = -11.66
O2Y = 23.58
O3X = -19.76
O3Y = 23.61
O4X = -24.06
O4Y = 23.63
B11X = 30.25
B11Y = 18.78
B12X = 16.69
B12Y = 18.75
B13X = 7.3
B13Y = 18.73
B14X = -11.6
B14Y = 18.69
B15X = -19.7
B15Y = 18.67
A4X = -27.25
A4Y = 18.66
N3X = 39.52
N3Y = 15.04
B10X = 30.28
B10Y = 14.91
D2X = 9.63
D2Y = 13.56
D1X = 7.36
D1Y = 13.5
C1X = -19.7
C1Y = 16.08
B1X = -27.26
B1Y = 16.02
M1X = -34.86
M1Y = 16.94
M2X = -38.6
M2Y = 10.68
B2X = -27.28
B2Y = 10.62
C2X = -19.7
C2Y = 10.62
C3X = -11.58
C3Y = 10.62
N2X = 41.85
N2Y = 11.84
N1X = 35.59
N1Y = -0.98
B9X = 30.41
B9Y = -1.49
C11X = 20.8
C11Y = -1.22
D4X = 13.99
D4Y = -1.17
D3X = 10.06
D3Y = -1.04
D5X = 10.13
D5Y = -4.48
D7X = 11.78
D7Y = -4.5
D6X = 14.05
D6Y = -4.54
D8X = 18.53
D8Y = -4.6
B3X = -27.35
B3Y = -7.24
C4X = -19.7
C4Y = -5.9
C5X = -11.55
C5Y = -4.48
M3X = -38.97
M3Y = -12.58
A1X = -27.37
A1Y = -12.7
B4X = -11.54
B4Y = -12.82
B5X = 1.96
B5Y = -12.92
B6X = 8.47
B6Y = -12.97
B7X = 11.84
B7Y = -12.99
B8X = 18.72
B8Y = -13.05
A3X = 30.5
A3Y = -13.13
C7X = 8.41
C7Y = -16.2
C8X = 30.43
C8Y = -16.26
A5X = 1.78
A5Y = -23.5
C9X = 20.07
C9Y = -23.81
C10X = 30.32
C10Y = -21.05
#print(O2Y-C3Y)






