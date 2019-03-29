# punto 4 primo hermano
a=int(input("Por favor ingrese un numero para saber si es primo hermano "))
def primoh():
  if a%6==0:
     print("El numero", a, "no es primo hermano")
  else:
    i=0
    n=a+1
    for m in range (1,n+1):
      if n%m==0:
        i=i+1
    if i>2:
      print("El numero", a, "no es primo hermano")
    else:
      print("El numero", a, "es primo hermano")

primoh()
      
