import random as rd 
listas = []
N= [30]
def genera(n, min, max):
    return [rd.randint(min, max) for i in range(n)]

for i in N:
    listas.append(genera(i, 1, 1000))

print (listas)