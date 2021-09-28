
bpm = 1
age = int(input("Age: "))
max_t_pl=220-age
Z3=max_t_pl*0.7
Z4=max_t_pl*0.8
Z5=max_t_pl*0.9
CZ3=0
CZ4=0
CZ5=0
max_pl=0
min_pl=max_t_pl
Cbpm=0
# 0 terminates execution.
while bpm != 0:
    bpm = int(input("bpm: "))
    if bpm!=0:
        Cbpm+=1
        if bpm>max_pl:
            max_pl=bpm
        elif bpm<min_pl:
            min_pl=bpm
        if bpm>Z5:
            CZ5+=1
        elif bpm>Z4:
            CZ4+=1
        elif bpm>Z3:
            CZ3+=1

print("Result")
print("Zona3: (>",Z3,"): ",round(CZ3/Cbpm*100),"%")
print("Zona4: (>",Z4,"): ",round(CZ4/Cbpm*100),"%")
print("Zona5: (>",Z5,"): ",round(CZ5/Cbpm*100),"%")
print("Max value: ",max_pl)
print("Min value: ",min_pl)
    
