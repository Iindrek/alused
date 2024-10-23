import math                                #can also do: "from math import pi" and use just "pi" instead of math.pi 

r = float(input("Sisesta ringi raadius: "))
C = round(math.pi * 2 * r, 2)
S = round(math.pi * r * r, 2)

print("Ringi raadius on: ", r)

print("Ringi ümbermõõt on: ", C)

print("Ringi pindala on: ", S)