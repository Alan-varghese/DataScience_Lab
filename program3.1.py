import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
plt.pie(y,autopct='%1.1f%%')
plt.show()