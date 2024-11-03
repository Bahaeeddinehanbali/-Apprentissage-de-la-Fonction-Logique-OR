
import random
from time import sleep
w1 = random.uniform(0, 1)
w2 = random.uniform(0, 1)
s=0
n = 0.7
L1 = [0,0,1,1]
L2 = [0,1,0,1]
def f(x):
    return 1 if x >= 0 else 0
def OR(x1, x2):
    s = (x1*w1) + (x2*w2) - 0.5
    return f(s)
def ran(x,y):
    global w1, w2,n
    if OR(x1, x2) - (x1 or x2) != 0:
        w1 = w1+n*((x or y)-OR(x,y))*x
        w2 = w2+n*((x or y)-OR(x,y))*y
        print(f" ++ Valeur nouvelle  de poids w1 = {w1} et w2 = {w2}")
    return OR(x,y)

while True:
    erreur = 0
    print(f"-- Valeur de poids w1 = {w1} et w2 = {w2}")
    for x1, x2 in zip(L1, L2):
        if OR(x1, x2) == (x1 or x2):
            print(f" VV {x1,x2}")
            sleep(1)
            continue
        else:
            print(f" FF {x1, x2}")
            sleep(1)
            ran(x1, x2)
            erreur +=1

    if erreur == 0:
         print("Les poids corrects sont trouvés!")
         break

print(f" \n ********  les valeur de poids trouve est w1={w1} and w2={w2} ********* \n")
print(f"0 OR 0 = {OR(0,0)} \n")
print(f"0 OR 1 = {OR(0,1)} \n")
print(f"1 OR 0 = {OR(1,0)} \n")
print(f"1 OR 1 = {OR(1,1)} \n")


