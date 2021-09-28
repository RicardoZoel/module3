Co=0
i=0
n=0

Co = int(input("Input capital: "))
i = float(input("Input interest: "))/100
n = int(input("Input years: "))
count=1
while count<=n:
    quota=Co*((i*pow(1+i,n))/(pow(1+i,n) -1))
    print("Year", count," - quota: ",quota,"€ - Paid out: ")
    count+=1
