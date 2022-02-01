import random
from tkinter import *
from tkinter import messagebox as MessageBox

def empate():
    MessageBox.showinfo("¡EMPTATE!", "Has empatado, ¡no esta mal!, pueder probar de nuevo", icon="warning")

def ganas():
    MessageBox.showinfo("¡¡GANASTE!!", "¡Bieeeen Ganaste!", icon="info")

def pierdes():
    MessageBox.showinfo("¡PERDISTE!", "¡Vaya!, pruba de nuevo ¡tu puedes!", icon="error")

def btnpiedra():
    ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
    lbl_Piedra = Label(raiz, image = valorPiedraget, background="dimgray").place(x=250, y=300)
    lbl_PiedraRandom = Label(raiz, image = ImagenRandom, background="dimgray").place(x=1150, y=300)
    if ImagenRandom == valorPiedraget:
        empate()
    elif ImagenRandom == valorTijeraget:
        ganas()
    elif ImagenRandom == valorLagartoget:
        ganas()
    elif ImagenRandom == valorSpockget:
        pierdes()
    elif ImagenRandom == valorPapelget:
        pierdes()

def btnpapel():
    ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
    lbl_Papel = Label(raiz, image= valorPapelget, background="dimgray").place(x=250, y=300)
    lbl_PapelRandom = Label(raiz, image=ImagenRandom,background="dimgray").place(x=1150, y=300)
    if ImagenRandom == valorPapelget:
        empate()
    elif ImagenRandom == valorPiedraget:
        ganas()
    elif ImagenRandom == valorSpockget:
        ganas()
    elif ImagenRandom == valorTijeraget:
        pierdes()
    elif ImagenRandom == valorLagartoget:
        pierdes()

def btntijera():
    ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
    lbl_Tijera = Label(raiz, image= valorTijeraget, background="dimgray").place(x=250, y=300)
    lbl_TijeraRandom = Label(raiz, image=ImagenRandom, background="dimgray").place(x=1150, y=300)
    if ImagenRandom == valorTijeraget:
        empate()
    elif ImagenRandom == valorPapelget:
        ganas()
    elif ImagenRandom == valorLagartoget:
        ganas()
    elif ImagenRandom == valorSpockget:
        pierdes()
    elif ImagenRandom == valorPiedraget:
        pierdes()

def btnlagarto():
    ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
    lbl_Lagarto = Label(raiz, image= valorLagartoget, background="dimgray").place(x=250, y=300)
    lbl_LagartoRandom = Label(raiz, image=ImagenRandom, background="dimgray").place(x=1150, y=300)
    if ImagenRandom == valorLagartoget:
        empate()
    elif ImagenRandom ==  valorSpockget:
        ganas()
    elif ImagenRandom == valorPapelget:
        ganas()
    elif ImagenRandom == valorTijeraget:
        pierdes()
    elif ImagenRandom == valorPiedraget:
        pierdes()

def btnspock():
    ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
    lbl_Spock = Label(raiz, image= valorSpockget, background="dimgray").place(x=250, y=300)
    lbl_SpockRandom = Label(raiz, image=ImagenRandom, background="dimgray").place(x=1150, y=300)
    if ImagenRandom == valorSpockget:
        empate()
    elif ImagenRandom == valorTijeraget:
        ganas()
    elif ImagenRandom == valorPiedraget:
        ganas()
    elif ImagenRandom == valorLagartoget:
        pierdes()
    elif ImagenRandom == valorPapelget:
        pierdes()





raiz = Tk()
raiz.title("Tablero")
raiz.geometry("1600x1000")
raiz.config(bg="dimgray")
raiz.resizable(False, False)
raiz.iconbitmap("img/icono2.ico")


dic = {'1': PhotoImage(file="img/Piedra.png"), '2': PhotoImage(file="img/Papel.png"), '3': PhotoImage(file="img/Tijeras.png"), '4': PhotoImage(file="img/Lagarto.png"), '5': PhotoImage(file="img/Spock.png")}
valorPiedraget = dic.get('1')
valorPapelget = dic.get('2')
valorTijeraget = dic.get('3')
valorLagartoget = dic.get('4')
valorSpockget = dic.get('5')
Versus = PhotoImage(file="img/versus.png")
Usuario = PhotoImage(file="img/usuario.png")
Ordenador = PhotoImage(file="img/ordenador.png")


btn_Piedra = Button(raiz, image = valorPiedraget, background="dimgray", foreground="dimgray", cursor="plus", command=btnpiedra).place(x=100, y=750)
btn_Papel = Button(raiz, image = valorPapelget, background="dimgray", foreground="dimgray", cursor="plus", command=btnpapel).place(x=400, y=750)
btn_Tijera = Button(raiz, image = valorTijeraget, background="dimgray", foreground="dimgray", cursor="plus", command=btntijera).place(x=700, y=750)
btn_Lagarto = Button(raiz, image = valorLagartoget, background="dimgray", foreground="dimgray", cursor="plus", command=btnlagarto).place(x=1000, y=750)
btn_Spock = Button(raiz, image = valorSpockget, background="dimgray", foreground="dimgray", cursor="plus", command=btnspock).place(x=1300, y=750)
lbl_Versus = Label(raiz, image= Versus, background="dimgray").place(x=640, y=200)
lbl_UsuarioImagen = Label(raiz, image = Usuario, background="dimgray").place(x=220, y=240)
lbl_OrdenadorImagen = Label(raiz, image= Ordenador, background="dimgray").place(x=1120, y=240)
lbl_UsuarioTexto = Label(raiz, text="USUARIO", background="dimgray", foreground="black", font=("Arial Black", 18)).place(x=280, y=240)
lbl_OrdenadorTexto = Label(raiz, text="ORDENADOR", background="dimgray", foreground="black", font=("Arial Black", 18)).place(x=1180, y=240)




raiz.mainloop()