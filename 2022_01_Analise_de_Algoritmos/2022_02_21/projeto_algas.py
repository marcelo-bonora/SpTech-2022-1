from matplotlib import pyplot as plt
import sys
import time

listTempo = [3, 6, 3, 3, 3]
listTamanhoByte = []

def eficienciaAlgoritmo(x):
    tempo_inicial = (time.time())
    list = []
    tamanhoList = 0
    countList = 0

    for item in x:
        list.append(item)
        countList += 1

    listTamanhoByte.append(sys.getsizeof(list))

    for i in range(countList):
        list.pop()

    tempo_final = (time.time())
    # listTempo.append(tempo_final - tempo_inicial)
    print(tempo_inicial)
    print(tempo_final)

eficienciaAlgoritmo(range(100000, 600000, 100000))
eficienciaAlgoritmo(range(1000, 6000, 100))
eficienciaAlgoritmo(range(100, 600, 100))
eficienciaAlgoritmo(range(10, 60, 10))
eficienciaAlgoritmo(range(1000000, 6000000, 1000000))

print(listTempo)
print(listTamanhoByte)
    
plt.bar(listTempo, listTamanhoByte)
plt.show()