a=list(input("ingresar numero de dos cifras "))
b = ''.join(a)
print("el numero ingresado es ",b)
a.reverse()
c = ''.join(a)
print("el numero ingresado inverso es ",c)

x=list(input("ingresar numero de tres cifras "))
y = ''.join(x)
print("el numero ingresado es ",y)
x.reverse()
z = ''.join(x)
print("el numero ingresado inverso es ",z)

primer=int(input("ingresar el primer numero "))
segundo=int(input("ingresar el segundo numero "))
if primer==0 or segundo==0:
    print("no se pueden ingresar como valor cero")
else:
    suma=primer+segundo
    print("la suma de ",primer,"+",segundo, "es ",suma)
    resta=primer-segundo
    print("la resta de ",primer,"-",segundo, "es ",resta)
    division=primer/segundo
    print("la division de ",primer,"/",segundo, "es ",division)
    multiplicacion=primer*segundo
    print("la multiplicacion de ",primer,"x",segundo, "es ",multiplicacion)
    potencia=primer**segundo
    print("la potencia de ",primer,"elevado a ",segundo, "es ",potencia)
if primer<0 or segundo<0:
    print("no se puede sacar raiz de valores negativos")
else:
    raiz1=primer**0.5
    print("la raiz de ",primer,"es ",raiz1)
    raiz2=segundo**0.5
    print("la raiz de ",segundo,"es ",raiz2)

    

