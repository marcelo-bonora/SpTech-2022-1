import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import turtle
import sys
import time


print("----- Solução Interativa -----")
def lista_soma(num_lista):
    tot_soma = 0
    for i in num_lista:
        tot_soma = tot_soma + i
    return tot_soma

print(lista_soma([1,3,5,7,9]))


print("----- Solução Recursiva -----")
def lista_soma_recursivo(num_lista):
    if len(num_lista) == 1:
        return num_lista[0]
    else:
        return num_lista[0] + lista_soma_recursivo(num_lista[1:])

print(lista_soma([1,3,5,7,9]))


print("----- Cálculo Fatorial(Recursivo) -----")
def fatorial(n):
    if n <= 0 : return 1
    print("Chamando fatorial de ", n - 1)
    return n * fatorial(n - 1)
f = fatorial(5)

print("Fatorial de 5 = ", f)


print("----- Desafio de Recursão -----")
lstValores = [50, 60, 70, 80, 90, 100]
lstTempo = []
lstEspaco = []


my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def lst_draw_spiral(lstValores):
    for i in lstValores:
        tempo_inicial = (time.time())
        lstEspaco.append(sys.getsizeof(draw_spiral(my_turtle, i))+ i)
        tempo_final = (time.time())
        lstTempo.append(tempo_final - tempo_inicial)
    print(lstEspaco)
    print(lstTempo)
    b = np.matrix((lstTempo, lstEspaco))
    b_asarray = np.asarray(b)
    plt.plot(b_asarray)


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.left(90)
        draw_spiral(my_turtle, line_len - 5)

# my_win.exitonclick()
lst_draw_spiral(lstValores)

plt.show()




