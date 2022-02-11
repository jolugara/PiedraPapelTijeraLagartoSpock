from tkinter import *
from Logica import Logica

# Creamos el panel
raiz = Tk()

# Le ponemos el nombre al panel
raiz.title("Tablero")

# Le damos un tamaño al panel
raiz.geometry("1600x1000")

# Le damos el color de fondo al panel
raiz.config(bg="dimgray")

# Hacemos que el panel no se pueda no agrandar ni disminuir del tamaño que se le dio
raiz.resizable(False, False)

# Le damos un icono al panel
raiz.iconbitmap("img/icono2.ico")

# Creamos un diccionario en el que guardaremos las imagenes con un numero que sera su id a la hora de llamalos en los paneles
dic = {'1': PhotoImage(file="img/Piedra.png"), '2': PhotoImage(file="img/Papel.png"), '3': PhotoImage(file="img/Tijeras.png"), '4': PhotoImage(file="img/Lagarto.png"), '5': PhotoImage(file="img/Spock.png")}
valorPiedraget = dic.get('1')
valorPapelget = dic.get('2')
valorTijeraget = dic.get('3')
valorLagartoget = dic.get('4')
valorSpockget = dic.get('5')

# Logo de VS
Versus = PhotoImage(file="img/versus.png")

# Logo del usuario
Usuario = PhotoImage(file="img/usuario.png")

#Logo del ordenador
Ordenador = PhotoImage(file="img/ordenador.png")

# Creamos la variable logica a la que le indicamos que guardara nusetro objeto Logica
logica = Logica()

# Funcion que se ejecuta al pulsar el boton pierdra y llamara a la funcion btnpiedra de nuestro objeto Logica,
# asi en todas las funciones
def btnpiedra():
    btnpiedra = logica.btnpiedra(raiz)

def btnpapel():
    btnpapel = logica.btnpapel(raiz)

def btntijera():
    btntijera = logica.btntijera(raiz)

def btnlagarto():
    btnlagarto = logica.btnlagarto(raiz)

def btnspock():
    btnspock = logica.btnspock(raiz)


# Boton piedra al que se le introduce el panel en el que queremos que aparezca en este caso raiz, se le da la imagen que queremos que aparezca en el boton atravez del diccionario que creamos mas arriba
# le damos un color de fondo, le indicamos que al pasar por encima del boton el cursor cambia a una forma distinta y le indicamos atravez de command la funcion que queremos que se ejecute al presionalo
# asi en todos los botones
btn_Piedra = Button(raiz, image = valorPiedraget, background="dimgray", foreground="dimgray", cursor="plus", command=btnpiedra).place(x=100, y=750)


btn_Papel = Button(raiz, image = valorPapelget, background="dimgray", foreground="dimgray", cursor="plus", command=btnpapel).place(x=400, y=750)


btn_Tijera = Button(raiz, image = valorTijeraget, background="dimgray", foreground="dimgray", cursor="plus", command=btntijera).place(x=700, y=750)


btn_Lagarto = Button(raiz, image = valorLagartoget, background="dimgray", foreground="dimgray", cursor="plus", command=btnlagarto).place(x=1000, y=750)


btn_Spock = Button(raiz, image = valorSpockget, background="dimgray", foreground="dimgray", cursor="plus", command=btnspock).place(x=1300, y=750)

# Creamos un label para la imagen VS que indicamos que aparezca en nuestro panel raiz. le damos un color de fondo y le damos la posicion en la que queremos que aparezca la imagen dentro del panel con .place,
# asi en todos los labels
lbl_Versus = Label(raiz, image= Versus, background="dimgray").place(x=640, y=200)

lbl_UsuarioImagen = Label(raiz, image = Usuario, background="dimgray").place(x=220, y=240)

lbl_OrdenadorImagen = Label(raiz, image= Ordenador, background="dimgray").place(x=1120, y=240)

lbl_UsuarioTexto = Label(raiz, text="USUARIO", background="dimgray", foreground="black", font=("Arial Black", 18)).place(x=280, y=240)

lbl_OrdenadorTexto = Label(raiz, text="ORDENADOR", background="dimgray", foreground="black", font=("Arial Black", 18)).place(x=1180, y=240)

# Hacemos que se ejecute el programa
raiz.mainloop()