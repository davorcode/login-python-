Usuarios = {}

def registro (): 
    nombre = input ("ingresa tu nombre")
    contraseña = input ("ingresa tu contraseña")
    while contraseña.strip() == "":
        contraseña = input ("contraseña incorrecta, escribela de vuelta")
    Usuarios[nombre] = contraseña 

def mostrar_usuarios ():
    if not Usuarios: 
        print ("no hay usuarios registrados")
        return
    for usuario, contraseña in Usuarios.items():
        print(usuario, contraseña)

def login ():
    nombre = input ("ingresa tu nombre correspondiente")
    contraseña = input ("ingresa tu contraseña")
    if nombre in Usuarios:
        if  contraseña == Usuarios[nombre]:
            print ("bienvenido")
        else: 
            print ("contraseña incorrecta")
    else:
        print ("usuario no encontrado ")

registro()
mostrar_usuarios()
login()
        
