containerFila=[]

containerFila.append(10)
containerFila.append(15)
containerFila.append(21)

for i in containerFila:
    print(i)

print("AFTER POP")

containerFila.pop(0)
for i in containerFila:
    print(i)
