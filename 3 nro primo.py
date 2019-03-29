#punto 3 numero primo
a=int(input("Por favor ingrese un numero para saber si es primo o no "))
def primo():
  i=0
  for n in range(1,a+1):
    if a%n==0:
     i=i+1
  if i>2:
    print("El numero ingresado fue:", a, "y no es primo")
  else:
    print("El numero ingresado fue:", a, "y es primo")
primo()
