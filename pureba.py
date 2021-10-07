a = [12,0,39,50,1]

first = a[0]

i = 0
j = 1
while i < len(a):
    if a[i] < first:
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
    i += 1

print(a)