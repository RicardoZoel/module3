
DNI=input("DNI: ")
while True:
    DNI=input("DNI: ")
    num=DNI[:-1]
    letter=DNI[-1]
    if len(DNI)!=9 and DNI[:-1].isdigit():
        num=int(DNI[:-1])
        break
    else:
        print("Format incorrect")
Leter="TRWAGMYFPDXBNIZSQVHKCKE"
if DNI[-1].upper()==Leter[numL]:
    print("El DNI esta bien")
else:
    print("El DNI no esta bien")