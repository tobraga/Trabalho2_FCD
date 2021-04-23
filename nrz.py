import numpy as np
import matplotlib.pyplot as plt


def nrz(vetor):
	for i in range(0,len(vetor)):
		plt.plot([i,i+1], [vetor[i],vetor[i]], 'yo-', color='k')
		if i != 0:
			if vetor[i-1] != vetor[i]:
				plt.plot([i,i], [0,1], 'yo-', color='k')


#NonReturnZero

binario = [1,0,1,1,0]
nrz(binario)
plt.show()