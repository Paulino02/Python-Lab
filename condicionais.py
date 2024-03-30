#condicionais
'''
x = input("digite um numero: ")
i = input("digite um numero: ")
if x < i:
    print("x eh menor ou igual", i)
#print("resto do código")
elif x == i:
    print("x is equal to",i)
else:
    print("x eh maior que",i)
'''
#banco de dados 
DevOps = ["jenkins", "ansible", "bash", "puppet", "docker", "kubernetes", "terraform"] #lista -> [] 
Development = ("java", "nodejs", "javascript", ".net", "python") # estrutura de dados -> ()
temp = {"nome":"tps", "Skill":"AI", "code":1234} # dicionario -> {}
temp2 ={"nome":"tp", "Skill":"FinOps", "code":12345} #dicionario -> {}

usr_skill = input("enter your desired skill: ")
# checar se existe essa skill no banco de dados

if usr_skill in DevOps:
    print(f"we have {usr_skill} in Devops team")
elif usr_skill in Development:
    print(f"we have {usr_skill} in Development team")
elif (usr_skill in temp.values()) or (usr_skill in temp2.values()):
    print(f"nos ja contratamos empregados com {usr_skill} skill")
else:
    print("skill not found")
    print("please check if you have entered value in capitalize or check the spelling.")