#Estrutura de repetição FOR
'''
planeta = "terra"
for i in planeta:
    print(i)

vacinas = ("covid-19", "pfizer", "sputnik v", "astrazenica")

for vac in vacinas:
    print(f"{vac}vacina tras imunidade contra covid 19")
'''
import time
# while loop
x = 2
while True:
    print("value of X is", x)
    print("looping")
    x*=2
    time.sleep(1)