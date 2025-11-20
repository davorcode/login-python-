USUARIOS = {}

def registro (): 
    nombre = input ("ingresa tu nombre")
    while nombre.strip () == "" or nombre in USUARIOS:
        nombre = input ("el nombre está vacio o ya existe, ingresá otro")
    contraseña = input ("ingresa tu contraseña")
    while contraseña.strip() == "":
        contraseña = input ("contraseña incorrecta, escribela de vuelta")
    USUARIOS[nombre] = contraseña 

def mostrar_usuarios ():
    if not USUARIOS: 
        print ("no hay usuarios registrados")
        return
    for usuario, contraseña in USUARIOS.items():
        print(usuario, contraseña)

def login ():
    nombre = input ("ingresa tu nombre correspondiente")
    contraseña = input ("ingresa tu contraseña")
    if nombre in USUARIOS:
        if  contraseña == USUARIOS[nombre]:
            print ("bienvenido")
        else: 
            print ("contraseña incorrecta")
    else:
        print ("usuario no encontrado ")

registro()
mostrar_usuarios()
login()
        
