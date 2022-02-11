import re

varx = []
vary = []

def sum_of_n_init():
    acumul_acelerate = 0
    for i in range(1, 11):
        acumul_acelerate = acumul_acelerate + i
        varx.append(acumul_acelerate)
        vary.append(i)

def sum_of_n_init_two(n):
    acumul_acelerate = 0
    for i in range(1, n+1):
        acumul_acelerate = acumul_acelerate + i
    return acumul_acelerate

velocity_test = 50000

sum_of_n_init()
print(sum_of_n_init_two(velocity_test))
print(vary)
print(varx)


