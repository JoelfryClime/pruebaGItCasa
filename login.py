user = "joelfry"
password = 132101

while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = int(input("Ingrese su contraseña: "))
    
    if usuario == user and contrasena == password:
        print("Has podido entrar a tu cuenta con éxito")
        break
    else:
        print("Usuario o contraseña incorrecta. Vuelva a intentar")