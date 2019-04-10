#Best fit line code
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from random import randint


#This is Our Data generated randomly
x = [randint(0, 9) for p in range(0, 10)]
y = [randint(0, 9) for p in range(0, 10)]
x = np.asarray(x)
y = np.asarray(y)

def best_fit_line(x,y):
    x_best = ( ( mean(x)*mean(y) - mean(x*y) ) / (mean(x)**2 - mean(x**2)) )
    y_best = mean(y) - x_best*mean(x)
    return x_best ,y_best

x_best , y_best = best_fit_line(x,y)
best_line = [(x_best*i)+y_best for i in x]


predicted_x = [randint(0, 9) for p in range(0, 20)]
predicted_y = [(x_best*i)+y_best for i in predicted_x]


plt.scatter(predicted_x,predicted_y,color ='r')
plt.scatter(x,y)
plt.plot(x,best_line)
plt.show()
