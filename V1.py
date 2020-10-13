import matplotlib.pyplot as plt
import random
from xlrd import open_workbook
import math

Circle_X_list=[]
Circle_Y_list=[]
def frequencyCirclePlot(r):
    for q in range(0,48):

        radii=r # r is a variable
        r_x=x_data[q]
        r_y=y_data[q]
        Number=specialFre[q]
        r_x_max = r_x + radii
        r_x_min = r_x - radii
        r_y_max = r_y + radii
        r_y_min = r_y - radii
        Account=0
        '''
        print(q)
        print(Number)
        '''
        # To generate the exact number of points in the circle according to my data set 
        while Account< Number:

            r_Random_x = random.uniform(r_x_min, r_x_max)
            r_Random_y = random.uniform(r_y_min, r_y_max)
            distance=math.sqrt((r_Random_x - r_x)**2+(r_Random_y - r_y)**2)# to calculate distance in math
            
            if distance <=radii:
                #gathering random points in the circle 
                Circle_X_list.append(r_Random_x)
                Circle_Y_list.append(r_Random_y)
                Account=Account+1
                #print(Account)

# because the random number generates x and y coordiante in a sqaure around center of circle, we need to judge if points in circle, if not, generate random number again
            if distance > radii:
                continue


        """
        # to view visually whether points are in the circle 
        print("X:",end="")
        print(r_x)
        print("Y:",end="")
        print(r_y)
        """

x_data = []
y_data = []
fre=[]
specialFre=[]
x_volte = []
temp = []
wb = open_workbook('data.xlsx.')

for s in wb.sheets():
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        x_data.append(values[1])  # add position of observation points
        y_data.append(values[2])  # add position of observation points
        fre.append(values[3]) # add the number of walkers passed the observation points
        specialFre.append(values[4])

plt.figure(figsize=(10, 8))

plt.plot(x_data, y_data, ".", color='black', alpha=0.45, ms='10')# plot all observation points in black
# plot the position of gates of park in green
gate_x=[30.07,-27.25,-27.37,30.5,1.78]
gate_y=[23.44,18.66,-12.7,-13.13,-23.5]
plt.plot(gate_x,gate_y,".",color="green",ms=12)

frequencyCirclePlot(3)# assumed radius of circle is three, you can type a different r value

plt.title("Distribution of walkers when assume their active range is 30m")
plt.xlabel("Distance in eastern-western direction  /10m")
plt.ylabel("Distance in southern-northern direction /10m")
plt.plot(Circle_X_list,Circle_Y_list,".",color="blue",ms=1)
plt.show()









