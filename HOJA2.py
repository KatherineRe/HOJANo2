print("-------EJERCICIO 1-------")
print("Ingrese su contraseña")
Contraseña=input();
print("Ingrese nuevamente la contraseña")
contraseña2=input();
if Contraseña.lower()==contraseña2.lower():
        print("Contraseña correcta")
else:
        print("contraseña incorrecta")
  

print("-------EJERCICIO 2-------")
nombre=input("Cual es su nombre")
genero=input("Cual es su genero, M o H")

if genero =="M":
    if nombre.lower() < "m":
        grupo = "A"
    else:    
        grupo = "B"
else:
    if nombre.lower() >"n":
       grupo ="A"
    else:
        grupo = "B"
print("Su grupo es  "+ grupo)
