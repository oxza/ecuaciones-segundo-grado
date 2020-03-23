import os, msvcrt, math, time

abc = 1
while abc == 1:
    os.system("cls")
    a = int(input("Introduce el valor del primer número: "))
    os.system("cls")
    print(str(a) + "x²")

    b = int(input("Introduce el valor del segundo número: "))
    os.system("cls")
    if b >= 0:
        print(str(a) + "x²+" + str(b) + "x")
    else:
        print(str(a) + "x²" + str(b) + "x")

    c = int(input("Introduce el valor del tercer número: "))
    os.system("cls")
    if b >= 0 and c >= 0:
        print(str(a) + "x²+" + str(b) + "x+" + str(c))
    elif b >= 0 and c < 0:
        print(str(a) + "x²+" + str(b) + "x" + str(c))
    elif b < 0 and c >= 0:
        print(str(a) + "x²" + str(b) + "+" + str(c))
    else:
        print(str(a) + "x²" + str(b) + "x" + str(c))

    print("\nPresiona cualquier tecla para despejar la X")
    msvcrt.getch()
    os.system("cls")
    print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))

    rc = b**2 - 4 * a * c
    if rc == 0:
        print("\nX tiene un solo valor porque " + str(b) + "²" + " - 4 x " + str(a) + " x " + str(c) + " = " + str(rc) + ".")
        raiz_cuadrada = math.sqrt(rc)
        x = (-b + raiz_cuadrada) / (2 * a)
        print("\nEl valor de la X es " + str(x))
    elif rc > 0:
        print("\nX tiene dos valores porque " + str(b) + "²" + " - 4 x " + str(a) + " x " + str(c) + " = " + str(rc) + " y " + str(rc) + " es un número mayor que 0.")
        raiz_cuadrada = math.sqrt(rc)
        x1 = (-b + raiz_cuadrada) / (2 * a)
        x2 = (-b - raiz_cuadrada) / (2 * a)
        print("\nLos dos valores de la X son " + str(x1) + " y " + str(x2))
    else:
        print("\nLa ecuación no tiene solución porque " + str(b) + "²" + " - 4 x " + str(a) + " x " + str(c) + " = " + str(rc) + " y " + str(rc) + " no puede ser un número negativo.")
    
    time.sleep(4)
    print("\n\nPulsa cualquier tecla para volver al principio.")
    msvcrt.getch()
