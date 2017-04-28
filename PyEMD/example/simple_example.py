import numpy  as np
import pylab as plt
from PyEMD.EMD import EMD

t = np.linspace(0, 1, 200)
tt = t*t
s = np.cos(11*2*np.pi*tt) + 6*tt

IMF = EMD().emd(s,t)
N = IMF.shape[0]+1

plt.subplot(N,1,1)
plt.plot(t, s, 'r')
plt.title("Input signal: $S(t)=cos(22\pi t^2) + 6t^2$")
plt.xlabel("Time [s]")

for n, imf in enumerate(IMF):
    plt.subplot(N,1,n+2)
    plt.plot(t, imf, 'g')
    plt.title("IMF "+str(n+1))
    plt.xlabel("Time [s]")

plt.tight_layout()
plt.savefig('simple_example')
plt.show()
