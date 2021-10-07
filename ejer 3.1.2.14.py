blocks=int(input("Numbre of blocks: "))
height=0
cont=1
while cont<=blocks:
    height+=1
    blocks-= cont
    cont+=1
print("The height of the pyramid:", height)