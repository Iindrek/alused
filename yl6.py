a = float(input("Sisesta esimene arv: "))
b = float(input("Sisesta teine arv: "))
c = float(input("Sisesta kolmas arv: "))

if (a >= b) and (a >= c):
        suurim = a
elif (b >= a) and (b >= c):
        suurim = b
else:
        suurim = c
print("Suurim number on: ", suurim)