import random
vacinas = ["covid-19", "pfizer", "sputnik v", "astrazenica"]

random.shuffle(vacinas)
#print(vacinas)

sorte = random.choice(vacinas)
#print(sorte)

for vac in vacinas:
    print(f"***** testando vacina {vac}")
    if vac == sorte:
        print("########################")
        print(f"{sorte} vacina, test successful")
        print("########################")
        break
        

