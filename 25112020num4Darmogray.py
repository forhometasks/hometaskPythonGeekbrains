n = str(input("Введите число: "))
j = len(n)
c = 0
while j!=0:
    if n[c]>n[j-1]:
        max = n[c]
        min = n[j]
    j -= 1
    c += 1
print("Max: ", max)
print("Min: ", min)