import numpy as np
import matplotlib.pyplot as plt

plt.title('NRZ')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
def nrz(vetor):
	for i in range(0,len(vetor)):
		plt.plot([i,i+1], [vetor[i],vetor[i]], 'yo-', color='k')
		if i != 0:
			if vetor[i-1] != vetor[i]:
				plt.plot([i,i], [0,1], 'yo-', color='k')

#NonReturnZero

binario = [1,0,1,1,0]
#x = np.arange(1, len(binario) + 1, 1)
#plt.step(x, binario)
plt.xlabel(binario)
nrz(binario)
plt.show()