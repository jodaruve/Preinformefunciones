#punto 2 elevar dos numeros
def elevado():
  for i in range (0,2):
    i=i+1
    a=float(input("Por favor ingrese un numero "))
    b=float(input("Por favor ingrese un numero "))
    if i==1:
      n1=a**b
      print("El resultado es:", n1)
    elif i==2:
      n2=a**b
      print("El resultado es:", n2)
  if n1==n2:
    print("Los numeros son iguales")
  elif n1>n2:
    print(n1, "es mayor que:", n2)
  else:
    print(n2, "es mayor que:", n1)
elevado()
print ("fin")