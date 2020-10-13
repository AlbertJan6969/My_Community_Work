# My_Community_Work
Using traffic volume data  to advise some changes of arrangement of park in my community.



My goal is to use data of volume of interseciton of roads in the park to test which parts of park are crowded or not.
The application of this project can be use to judge layout of a city. With the traffic volume at hand, we could predict which parts of city are crowded where happens traffic jam the most. 

In my first approach, a point in a circle whose center lies in observation points with a varied radius can represent the possible appearance of a walker. Then I generated the number of random points that equaled to the number of people passed observation points in my data set to plot in the circle. In this case, we know whether an area is crowded or not by visually judging how dense points are in an area. (shown in PLF1.PNG)

My second way is to plot the possible appearance of walkers directly on roads instead of in a circle. Suppose that there are five observation points named A, B, C, D, and E, and A, B, C are collinear in eastern-western direction while C, D, E are collinear in southern-northern direction. As all observation points are the intersection of roads in the park, most observation points, like point C described above, lie exactly in the intersection of two segments (AB and DE ). Then I plotted and distributed the number of walkers passed the point C evenly in AB and DE. The number of random points on AB or DE, simulating the possible appearance of walkers on each road, would be half the number of walkers passed the point C because the volume needed to distribute evenly in the eastern-western direction and southern-northern direction Hence, after plotting all observation points by following the rules above, we know which roads are crowded and which roads are deserted.(shown in PLF2.PNG)

A simplified map of the park in my community: map.PNG
original traffic volume data in the park: data.xlsx
first approach: V1.py ,corresponding diagrams: F0.png F1.png F2.png F3.png F4.png
Second approach: V2.py, corresponding diagrams: Figure_1.png, Figure_2.png 
calculate_function.py is used to print values of variables to write in V2.py
