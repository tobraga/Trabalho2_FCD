import numpy as np
import matplotlib.pyplot as plt

plt.title('Manchester Diferencial')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
def manchester_diferencial(vetor):
	pos = -1
	for i in range(0,len(vetor)):
		if vetor[i] == 1:
			pos = (-1 if pos == 1 else 1)
		else:
			plt.plot([i,i], [1,-1], 'yo-', color='k')
		if pos == 1:
			if i != 0:
				plt.plot([i,i+0.5], [1,1], 'yo-', color='k')
			plt.plot([i+0.5,i+0.5], [1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+1], [-1,-1], 'yo-', color='k')
		else:
			if i != 0:
				plt.plot([i,i+0.5], [-1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+0.5], [1,-1], 'yo-', color='k')
			plt.plot([i+0.5,i+1], [1,1], 'yo-', color='k')
	plt.plot([0,0.5], [-1,-1], color='k')

#ManchesterDiferencial
binario = [0,1,0,0,1,1]
plt.xlabel(binario)
manchester_diferencial(binario)
plt.show()