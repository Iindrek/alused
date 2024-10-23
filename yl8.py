aasta = int(input("sisesta aasta: "))

if (aasta % 4 == 0 and aasta % 100 !=0) or (aasta % 400 == 0):
    print("aasta on liigaasta")
else:
    print("aasta ei ole liigaasta")