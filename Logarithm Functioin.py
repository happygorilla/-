import numpy as np
import matplotlib.pyplot as plt
time = np.arange(-10,10, 0.0001)
amplitude_log = np.log(time)
plt.plot(time, amplitude_log)
plt.title('Log Curve', color='b')
plt.xlabel('Time'+ r'$\rightarrow$')
plt.ylabel('Amplitude '+ r'$\rightarrow$')
plt.legend(['Log function'])
plt.grid()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt. show()