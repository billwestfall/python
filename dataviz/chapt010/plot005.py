import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,4))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_title('Main axes with child insert axes')
ax.plot(x, y[:,0])
ax.set_xlabel('Date')
ax.set_ylabel('Cumulative sum')
ax = fig.add_axes([0.15, 0.15, 0.3, 0.3])
ax.plot(x, y[:,1], color='g')
ax.set_xticks([])
plt.show()
