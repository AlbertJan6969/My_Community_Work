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
wb = open_workbook('data.xlsx')

for s in wb.sheets():
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        x_data.append(values[1])  # x coordinate of observation points
        y_data.append(values[2])  # y coordinate of observation points 
        fre.append(values[3]) # number of walkers passed the observation points 
        specialFre.append(values[4]) # average value of number of walkers passsed the observation points 
# copy the text generated from calculate_function.py
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
A2A = 45.0
O1A = 25.0
O2A = 23.0
O3A = 24.0
O4A = 32.0
B11A = 136.0
B12A = 141.0
B13A = 137.0
B14A = 136.0
B15A = 156.0
A4A = 228.0
N3A = 30.0
B10A = 167.0
D2A = 45.0
D1A = 45.0
C1A = 138.0
B1A = 135.0
M1A = 93.0
M2A = 142.0
B2A = 149.0
C2A = 152.0
C3A = 170.0
N2A = 30.0
N1A = 30.0
B9A = 199.0
C11A = 74.0
D4A = 86.0
D3A = 89.0
D5A = 84.0
D7A = 93.0
D6A = 80.0
D8A = 72.0
B3A = 144.0
C4A = 140.0
C5A = 160.0
M3A = 84.0
A1A = 165.0
B4A = 182.0
B5A = 193.0
B6A = 186.0
B7A = 180.0
B8A = 185.0
A3A = 246.0
C7A = 122.0
C8A = 177.0
A5A = 187.0
C9A = 80.0
C10A = 80.0
C6X=2.15
C6Y=-0.31
V=1
x_set=[]
y_set=[]

# the following function uses to plot points on some lines with a slope, which doesn't equal to zero
def calculateLine(AX,AY,BX,BY):
    K=(BY-AY)/(BX-AX)
    x_Line_point=random.uniform(AX,BX)
    y_line_point=K*(x_Line_point-AX)+AY
    #print(x_Line_point)
    #print(y_line_point)
    x_set.append(x_Line_point)
    y_set.append(y_line_point)

# B14
# Find four points or three points nearby. They are B13 B15 O2 C3

Account=0
while Account<B14A/V: # number 'V' controls the total number of points plotted in the graph
    a = random.uniform(0, 10)
    # the random number 'a' enables us to plot random points evenly in southern-northern direction and eastern-western direction
    if a >= 5:
        Value_x = random.uniform(B15X, B13X) # random x coordinate
        Value_y = B15Y # fixed y coordinate because B15Y=B13Y
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = C3X # fixed y coordinate because C3X=O2X
        Value_y = random.uniform(C3Y, O2Y) # random y coordiante
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B4
# Find the point nearby . They are C5 A1 B5

Account=0
while Account<B4A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(A1X, B5X) # here need a change
        Value_y = B4Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B4X # here need a change
        Value_y = random.uniform(B4Y, C5Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1

# C2
Account=0
while Account<C2A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B2X, C3X) # here need a change
        Value_y = C2Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = C2X # here need a change
        Value_y = random.uniform(C4Y, C1Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1

# B1
Account=0
while Account<B1A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B1X, C1X) # here need a change
        Value_y = B1Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B2X # here need a change
        Value_y = random.uniform(B2Y, A4Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B2
Account=0
while Account<B2A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(M2X, C2X) # here need a change
        Value_y = B2Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B2X # here need a change
        Value_y = random.uniform(B3Y, B1Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# A1
Account=0
while Account<A1A: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(M3X, B4X) # here need a change
        Value_y = A1Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = A1X # here need a change
        Value_y = random.uniform(A1Y, B3Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B15
Account=0
while Account<B15A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(A4X, B14X) # here need a change
        Value_y = B15Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B15X # here need a change
        Value_y = random.uniform(C1Y, O3Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# C1
Account=0
while Account<C1A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B1X, C1X) # here need a change
        Value_y = C1Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = C1X # here need a change
        Value_y = random.uniform(C2Y, B15Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# C3
Account=0
while Account<C3A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(C2X, C3X) # here need a change
        Value_y = C3Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = C3X # here need a change
        Value_y = random.uniform(C5Y, B14Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B5
Account=0
while Account<B5A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B4X, B6X) # here need a change
        Value_y = B5Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B5X # here need a change
        Value_y = random.uniform(A5Y, C6Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B13
Account=0
while Account<B13A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B14X, B12X) # here need a change
        Value_y = B13Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B13X # here need a change
        Value_y = random.uniform(D1Y, O1Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# D3
Account=0
while Account<D3A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(D3X, D4X) # here need a change
        Value_y = D3Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = D3X # here need a change
        Value_y = random.uniform(D5Y, D2Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# D4
Account=0
while Account<D4A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(D3X, C11X) # here need a change
        Value_y = D4Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = D4X # here need a change
        Value_y = random.uniform(D6Y, D4Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# D6
Account=0
while Account<D6A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(D7X, D8X) # here need a change
        Value_y = D6Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = D6X # here need a change
        Value_y = random.uniform(D6Y, D4Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# D7
Account=0
while Account<D7A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(D5X, D6X) # here need a change
        Value_y = D7Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = D7X # here need a change
        Value_y = random.uniform(B7Y, D7Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B6
Account=0
while Account<B6A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B5X, B7X) # here need a change
        Value_y = B6Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B6X # here need a change
        Value_y = random.uniform(C7Y, B6Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B7
Account=0
while Account<B7A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B6X, B8X) # here need a change
        Value_y = B7Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B7X # here need a change
        Value_y = random.uniform(B7Y, D7Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B8
Account=0
while Account<B8A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B7X, A3X) # here need a change
        Value_y = B8Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B8X # here need a change
        Value_y = random.uniform(B8Y, D8Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B11
Account=0
while Account<B11A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B12X, B11X) # here need a change
        Value_y = B11Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B11X # here need a change
        Value_y = random.uniform(B10Y, A2Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B10
Account=0
while Account<B10A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B10X, N3X) # here need a change
        Value_y = B10Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B10X # here need a change
        Value_y = random.uniform(B9Y, B11Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# B9
Account=0
while Account<B9A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(C11X, N1X) # here need a change
        Value_y = B9Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = B9X # here need a change
        Value_y = random.uniform(A3Y, B10Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# A3
Account=0
while Account<A3A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(B8X, A3X) # here need a change
        Value_y = A3Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = A3X # here need a change
        Value_y = random.uniform(C8Y, B9Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# C8
Account=0
while Account<C8A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(C7X, C8X) # here need a change
        Value_y = C8Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = C8X # here need a change
        Value_y = random.uniform(C10Y, A3Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# O3
Account=0
while Account<O3A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(O4X, O2X) # here need a change
        Value_y = O3Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = O3X # here need a change
        Value_y = random.uniform(B15Y, O3Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# O2
Account=0
while Account<O2A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(O3X, O1X) # here need a change
        Value_y = O2Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = O2X # here need a change
        Value_y = random.uniform(B14Y, O2Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# O1
Account=0
while Account<O1A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        Value_x = random.uniform(O2X, A2X) # here need a change
        Value_y = O1Y # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account=Account+1
    if a <= 5:
        Value_x = O1X # here need a change
        Value_y = random.uniform(B13Y, O1Y) # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1

# M1
Account=0
while Account<M1A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        calculateLine(M1X,M1Y,A4X,A4Y)
        Account=Account+1
    if a <= 5:
        calculateLine(M1X, M1Y, M2X, M2Y)
        Account = Account + 1
# O4
Account=0
while Account<O4A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        calculateLine(O4X,O4Y,O3X,O3Y)
        Account=Account+1
    if a <= 5:
        calculateLine(O4X, O4Y, A4X, A4Y)
        Account = Account + 1

# N2
Account=0
while Account<N2A*3/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        calculateLine(N2X,N2Y,N3X,N3Y)
        Account=Account+1
    if a <= 5:
        calculateLine(N2X, N2Y, N1X, N1Y)
        Account = Account + 1
# M3
Account=0
while Account<M3A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        calculateLine(M3X,M3Y,M2X,M2Y)
        Account=Account+1
    if a <= 5:
        calculateLine(M3X, M3Y, A1X, A1Y)
        Account = Account + 1
# C9
Account=0
while Account<C9A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        calculateLine(C9X,C9Y,C10X,C10Y)
        Account=Account+1
    if a <= 5:
        calculateLine(C9X, C9Y, A5X, A5Y)
        Account = Account + 1
# C10
Account=0
while Account<C10A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        calculateLine(C10X,C10Y,C8X,C8Y)
        Account=Account+1
    if a <= 5:
        calculateLine(C10X, C10Y, C9X, C9Y)
        Account = Account + 1
# D1
Account=0
while Account<D1A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 5:
        calculateLine(D1X,D1Y,B13X,B13Y)
        Account=Account+1
    if a <= 5:
        calculateLine(D1X, D1Y, D2X, D2Y)
        Account = Account + 1
# D1
Account=0
while Account<D1A/V: # here need a change
    a = random.uniform(0, 10)
    if a >= 10*2/3:
        calculateLine(C4X,C4Y,C5X,C5Y)
        Account=Account+1
    if a <= 10*1/3:
        calculateLine(C4X, C4Y, B3X, B3Y)
        Account = Account + 1
    else:
        Value_x = C4X # here need a change
        Value_y = random.uniform(C4Y,C2Y)  # here need a change
        x_set.append(Value_x)
        y_set.append(Value_y)
        Account = Account + 1
# C11
Account=0
while Account<C11A/V: # here need a change
    calculateLine(C11X,C11Y,B12X,B12Y)
    Account=Account+1




















plt.figure(figsize=(10, 8))
plt.plot(x_data, y_data, ".", color='black', alpha=0.45, ms='10')# plot observation points
gate_x=[30.07,-27.25,-27.37,30.5,1.78]
gate_y=[23.44,18.66,-12.7,-13.13,-23.5]
plt.plot(gate_x,gate_y,".",color="green",ms=12)#plot the position of gates
plt.plot(x_set,y_set,"x",color="purple",alpha=0.75,ms=1)
plt.title("Distribution of walkers in roads")
plt.xlabel("Distance in eastern-western direction  /10m")
plt.ylabel("Distance in southern-northern direction /10m")
plt.show()


