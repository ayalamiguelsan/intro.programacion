#primer archivo

#Ejercicio 1
'''
print("hola mundo")
'''
#Ejercicio 2
'''
citizen=  'hola mundo'
print(citizen)
'''
#Ejercico 3
''''
nombre=input('introduce tu nombre:')
print+("soy"+nombre+"!")
'''
#Ejercicio 4
'''
print(((3+2)/(2*5))**2)
'''
#Ejercicio 5
'''
horas= float(input("cuantas horas trabajas: "))
pago= float(input("cuanto te pagan por hora: "))
print (pago*horas)
'''
#ejercicio 6
'''
n=int(input("numero entero "))
suma=(n*(n+1)/2)
print(suma)
'''
#Ejercicio 7
'''
p=input("peso corporal ")
e=input("estatura ")
imc=round(float(p)/float(e)**2,2)
print(imc)
'''
#Ejercicio 8
'''
n=int(input("numero entero "))
m=int(input("numero entero "))
c=(n/m)
print(c)
r=(n%m)
print(r)
'''
#Ejercicio 9
'''
c=float(input("inversion "))
a=float(input("interes anual "))
n=float(input("numero de años "))
inc=round(c*(a/100+1)**n,2)
print("capital obtenido",inc)
'''
#ejercicio 10
'''
payasos=float(input("numero de payasos "))
muñecas=float(input("numero de muñecas "))
p=112
m=75
inc=(p*m)
print("peso del paquete",inc)
'''
#ejercicio 11
'''
ahorros=float(input("ingresa la cantidad de dinero depositado"))
interes=0.04
formula=(ahorros*interes)
año1=round((ahorros-formula),2)
formula2=(ahorros*interes)
año2=round((ahorros-formula2),2)
formula3=(ahorros*interes)
año3=round((ahorros-formula3),2)
print("la cantidad de ahorros tras el primer año sera de: ",año1,"la cantidad de ahorros tras el primer año sera de: ",año2,"la cantidad de ahorros tras el primer año sera de: ",año3)
'''
#ejercicio 12
'''
panesv=int(input("ingresa el numero de panes vendidos que no son del dia: "))
pan=3000
descuento=0.4
formula1=(panesv*pan)
formula2=(formula1*descuento)
print("el percio habitual de",panesv,"panes es de",formula1,"pero al no ser del dia tienen descuento del 40%, por lo que pagarias",formula2 )
'''

#ejercicio 1
'''
n=int(input("digita el numero entero "))
suma=(n*(n+1)/2)
if suma>20:
  print("es un gran numero")
else:
  print(suma)
'''
#ejercicio 2
'''
n=int(input("numero entero "))
m=int(input("numero entero "))
c=(n/m)
print(c)
r=(n%m)
print(r)
if c<1:
  print("es un gran numero")
else c>1:    
  print(suma)
'''
#ejercicio 3
invertir =float(input("ingresa la cantidad a invertir: "))
interes=float(input("ingresa el interes anual: "))
años=float(input("ingresa el numero de años: "))
formula=(invertir*((interes/100)+1)**años)
if formula < 100000:
  print("baja rentabilidad")
elif 100000<formula>1000000:
  print("rentabilidad baja")
else:
  print("es una buena inversion")
  