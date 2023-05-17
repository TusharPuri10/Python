import numpy as np
import matplotlib.pyplot as plt
import re
i=1
j=1
file = open("time_week_{}_Q_{}.txt".format(i,j),'r')
input_size = []
time = []
for row in file:
    y,x = re.split("-",row)
    x = int(x)
    y = int(y)
    input_size.append(x)
    time.append(y)

largest = time[0]
k_largest_x = []
k_largest_y = []
# k_largest_x.append(largest)
# k_largest_y.append(input_size[0])


for i in range(len(time)):
    if largest < time[i]:
        largest = time[i]
        k_largest_x.append(input_size[i])
        k_largest_y.append(time[i])





plt.rcParams['figure.figsize'] = [5, 4]
plt.title("Line graph")
plt.scatter(input_size, time, color="blue")

plt.plot(k_largest_x,k_largest_y,color="red")
plt.xlabel("input size")
plt.ylabel("time(ns)")

plt.show()