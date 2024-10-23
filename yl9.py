def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False


def type_of_triangle(a,b,c):
    if a==b and b==c:
        print("Kolmnurk on võrdkülgne.")
    elif a==b or b==c or a==c:
        print("Kolmnurk on võrdhaarne.")
    else:
        print("kolmnurk on erikülgne")


side_a = float(input("a: "))
side_b = float(input("b: "))
side_c = float(input("c: "))


if is_valid_triangle(side_a, side_b, side_c):
    type_of_triangle(side_a, side_b, side_c)
else:
    print("Kolmnurk ei ole võimalik.")