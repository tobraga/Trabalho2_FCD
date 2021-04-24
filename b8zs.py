bits = []
n_bits = int(input('Digite o número de bits: '))
for i in range(0, n_bits):
    entrada = int(input("bit {} = ".format(i)))
    if entrada == 0 or entrada == 1:
        bits.append(entrada)
    else:
        print("permitido somente 0 e 1")
print("bits de entrada: {}".format(bits))
print("\n")
'''
#taxa de bits = 1 bps
taxa = 1
#amostra para cada bit
amostra = 1000
#tempo total necessário para o fluxo de bits
tempo = len(bits)/taxa
#amostra total necessário para todo fluxo de bits
am_total = amostra*len(bits)
#tempo para cada amostra
tp_amostra = tempo/am_total
#contador de 0's
cont = 0
'''
#admitimos, por padrão, que o lastbit é igual a 1.
def oposto_lastbit(lastbit):
    if lastbit == 1:
        lastbit = 0
        return lastbit 
    if lastbit == 0:
        lastbit = 1
        return lastbit 
        
lastbit = 1


count_zero = 0
for i in range(0, len(bits)):
    bit = bits[i]
    aux = bit
    if bit == 0:
        count_zero += 1
    else:
        count_zero = 0


    if count_zero == 8:
        bits[i-7] = 0
        bits[i-6] = 0
        bits[i-5] = 0
        bits[i-4] = lastbit
        bits[i-3] = oposto_lastbit(lastbit)
        lastbit = bits[i-3]
        bits[i-2] = 0
        bits[i-1] = lastbit
        bits[i] = oposto_lastbit(lastbit)

print("bits de saida: {}".format(bits))
