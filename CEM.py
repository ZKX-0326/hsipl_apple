from algorithm import CEM
import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('apple.jpg')
image = np.double(image)
cem = CEM(image)
plt.scatter(150,60,s=30,c='r')
plt.imshow(cem)