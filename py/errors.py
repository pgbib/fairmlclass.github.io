import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)

plt.xkcd()
plt.figure(1, figsize=(7.5,3.75))
plt.subplot(121)
plt.title("Random errors")
pos1 = np.random.uniform(-2,2,(20,2))
plt.plot(pos1[:,0],pos1[:,1], 'r+')
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.subplot(122)
plt.title("Systematic errors")
pos2 = np.random.uniform(-2,-1,(20,2))
plt.plot(pos2[:,0],pos2[:,1], 'r+', linewidth=20)
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.tight_layout()
plt.savefig('../assets/random_systematic.svg')
plt.savefig('../assets/random_systematic.png')

plt.figure(2, figsize=(3.75,3.75))
x = np.linspace(1,100,200)
y = 1.0/np.sqrt(x)
plt.subplot(111)
plt.plot(x,y)
plt.xlabel('Sample size')
plt.ylabel('Error')
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.xlim(1,100)
plt.ylim(0,1)
plt.savefig('../assets/error_rate.svg')
plt.savefig('../assets/error_rate.png')

