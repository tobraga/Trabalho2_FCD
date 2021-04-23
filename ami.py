import numpy as np
import matplotlib.pyplot as plt

plt.title('AMI')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
def ami(vetor):
	pos = 0
	for i in range(0,len(vetor)):
		if vetor[i] == 0:
			plt.plot([i,i+1], [0,0], 'yo-', color='k')
		else:
			if pos == 0:
				plt.plot([i,i], [0,1], 'yo-', color='k')
				plt.plot([i,i+1], [1,1], 'yo-', color='k')
				plt.plot([i+1,i+1], [0,1], 'yo-', color='k')
			else:
				plt.plot([i,i], [0,-1], 'yo-', color='k')
				plt.plot([i,i+1], [-1,-1], 'yo-', color='k')
				plt.plot([i+1,i+1], [0,-1], 'yo-', color='k')
			pos = 0 if pos == 1 else 1


#AMI
binario = [0,1,0,0,1,0]
#plt.plot2[0,1,0,0,1,0]
ami(binario)
plt.show()
#plt.show()
