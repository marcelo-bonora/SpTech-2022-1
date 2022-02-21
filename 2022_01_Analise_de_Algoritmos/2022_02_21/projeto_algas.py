from matplotlib import pyplot as plt
import sys
import time

listTempo = []
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
    listTempo.append(tempo_final - tempo_inicial)
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


# encoding: iso-8859-1

# import time
# import sys
# import matplotlib.pyplot as plt

# tempo_inicial = (time.time())

# def transaction(range):
#     x_points = []
#     y_points = []

#     lista = []

#     for item in range:
#         # time.sleep(0.1)
#         lista.append(item)
#         tempo_append = (time.time())

#         tempo_final = (tempo_append - tempo_inicial)
#         x_points.append(tempo_final*100)
#         y_points.append(sys.getsizeof(lista))


#     print(lista)
#     plt.bar(x_points, y_points)


# transaction(range(100000, 600000, 100000))
# transaction(range(1000, 6000, 100))
# transaction(range(100, 600, 100))
# transaction(range(10, 60, 10))
# transaction(range(1000000, 6000000, 1000000))

# plt.show()