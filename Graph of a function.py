import numpy as np
import matplotlib.pyplot as plt

I = np.arange(-2,2, 0.0001)
P = 2*I*I
plt.plot(I,P)
P = 4*I*I
plt.plot(I,P)
P = 8*I*I
plt.plot(I,P)
plt.title('P = I*I*R', color='y')
plt.xlabel('I'+ r'$\rightarrow$')
plt.ylabel('P '+ r'$\rightarrow$')
plt.legend(['R=2', 'R=4', 'R=8'])
plt.grid()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()