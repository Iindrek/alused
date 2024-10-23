def abc(a, b):
     
    if a <= b:
        return a
    else:
        return b
a = float(input("Sisesta esimene number: "))
b = float(input("Sisesta teine number: "))
print("Väiksem arv on: ")
print(abc(a, b))