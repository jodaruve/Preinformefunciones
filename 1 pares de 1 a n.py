#Punto 1 numeros impares de 1 a n
a=int(input("por favor ingrese hasta donde desea que llegue el conteo "))
def impar():
  for i in range (1,a+1):
    if i%2!=0:
      print (i)
impar()
print ("fin")