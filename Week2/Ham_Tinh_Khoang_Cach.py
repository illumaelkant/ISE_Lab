

import numpy as np
import math

x_1 = np.array([1,2,3,4,5])
x_2 = np.array([5,4,3,2,1])





def euclid_distance():
    sum = 0
    for i in range (len(x_1)):
        sum += (x_1[i] - x_2[i])**2
    print(f"The distance is {math.sqrt(sum)}")
    return sum

euclid_distance()

