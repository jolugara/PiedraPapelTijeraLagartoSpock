from tkinter import *
import random
from tkinter import messagebox as MessageBox


class Logica():

    def __init__(self):
        pass

    # Creamos la funcion de empate que llamamos en todas las funciones para en el caso que empate aparezca un mensaje de alerta de que empato
    def empate(self):
        MessageBox.showinfo("¡EMPTATE!", "Has empatado, ¡no esta mal!, pueder probar de nuevo", icon="warning")

    # Creamos la funcion de ganar que llamamos en todas las funciones para en el caso que empate aparezca un mensaje de alerta de que gane
    def ganas(self):
        MessageBox.showinfo("¡¡GANASTE!!", "¡Bieeeen Ganaste!", icon="info")

    # Creamos la funcion de perder que llamamos en todas las funciones para en el caso que empate aparezca un mensaje de alerta de que pierde
    def pierdes(self):
        MessageBox.showinfo("¡PERDISTE!", "¡Vaya!, pruba de nuevo ¡tu puedes!", icon="error")

    # Creamos la funcion btnpiedra que se le llama en main al pulsar el boton piedra
    def btnpiedra(self, raiz):

        # Le creamos el panel raiz
        self.raiz = raiz

         # Creamos un diccionario con todas las imagenes guardados por numeros
        self.dic = {'1': PhotoImage(file="img/Piedra.png"), '2': PhotoImage(file="img/Papel.png"),
               '3': PhotoImage(file="img/Tijeras.png"), '4': PhotoImage(file="img/Lagarto.png"),
               '5': PhotoImage(file="img/Spock.png")}
        valorPiedraget = self.dic.get('1')
        valorPapelget = self.dic.get('2')
        valorTijeraget = self.dic.get('3')
        valorLagartoget = self.dic.get('4')
        valorSpockget = self.dic.get('5')

        # Creamos una variable donde seleccionara una imagen random entre las 5 que tenemos
        self.ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])

        # Creamos la variable lbl_piedra que contiene un label que mostrara la imagen piedra en este caso del usuario en la posicion que le indicamos
        self.lbl_Piedra = Label(raiz, image=valorPiedraget, background="dimgray").place(x=250, y=300)

        # Creamos la variable lbl_PiedraRandom que contiene un label que mostrara la imagen random del ordenador en la posicion que le indicamos
        self.lbl_PiedraRandom = Label(raiz, image=self.ImagenRandom, background="dimgray").place(x=1150, y=300)

        # Realizamos un if en el que comprobamos las imagenes para mostrar el mensaje que creamos mas arriba si gana, pierde o empata
        if self.ImagenRandom == valorPiedraget:
            self.empate()
        elif self.ImagenRandom == valorTijeraget:
            self.ganas()
        elif self.ImagenRandom == valorLagartoget:
            self.ganas()
        elif self.ImagenRandom == valorSpockget:
            self.pierdes()
        elif self.ImagenRandom == valorPapelget:
            self.pierdes()

    def btnpapel(self, raiz):
        self.raiz = raiz
        self.dic = {'1': PhotoImage(file="img/Piedra.png"), '2': PhotoImage(file="img/Papel.png"),
               '3': PhotoImage(file="img/Tijeras.png"), '4': PhotoImage(file="img/Lagarto.png"),
               '5': PhotoImage(file="img/Spock.png")}
        valorPiedraget = self.dic.get('1')
        valorPapelget = self.dic.get('2')
        valorTijeraget = self.dic.get('3')
        valorLagartoget = self.dic.get('4')
        valorSpockget = self.dic.get('5')
        self.ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
        self.lbl_Papel = Label(raiz, image=valorPapelget, background="dimgray").place(x=250, y=300)
        self.lbl_PapelRandom = Label(raiz, image=self.ImagenRandom, background="dimgray").place(x=1150, y=300)
        if self.ImagenRandom == valorPapelget:
            self.empate()
        elif self.ImagenRandom == valorPiedraget:
            self.ganas()
        elif self.ImagenRandom == valorSpockget:
            self.ganas()
        elif self.ImagenRandom == valorTijeraget:
            self.pierdes()
        elif self.ImagenRandom == valorLagartoget:
            self.pierdes()

    def btntijera(self, raiz):
        self.raiz = raiz
        self.dic = {'1': PhotoImage(file="img/Piedra.png"), '2': PhotoImage(file="img/Papel.png"),
               '3': PhotoImage(file="img/Tijeras.png"), '4': PhotoImage(file="img/Lagarto.png"),
               '5': PhotoImage(file="img/Spock.png")}
        valorPiedraget = self.dic.get('1')
        valorPapelget = self.dic.get('2')
        valorTijeraget = self.dic.get('3')
        valorLagartoget = self.dic.get('4')
        valorSpockget = self.dic.get('5')
        self.ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
        self.lbl_Tijera = Label(raiz, image=valorTijeraget, background="dimgray").place(x=250, y=300)
        self.lbl_TijeraRandom = Label(raiz, image=self.ImagenRandom, background="dimgray").place(x=1150, y=300)
        if self.ImagenRandom == valorTijeraget:
            self.empate()
        elif self.ImagenRandom == valorPapelget:
            self.ganas()
        elif self.ImagenRandom == valorLagartoget:
            self.ganas()
        elif self.ImagenRandom == valorSpockget:
            self.pierdes()
        elif self.ImagenRandom == valorPiedraget:
            self.pierdes()

    def btnlagarto(self, raiz):
        self.raiz = raiz
        self.dic = {'1': PhotoImage(file="img/Piedra.png"), '2': PhotoImage(file="img/Papel.png"),
               '3': PhotoImage(file="img/Tijeras.png"), '4': PhotoImage(file="img/Lagarto.png"),
               '5': PhotoImage(file="img/Spock.png")}
        valorPiedraget = self.dic.get('1')
        valorPapelget = self.dic.get('2')
        valorTijeraget = self.dic.get('3')
        valorLagartoget = self.dic.get('4')
        valorSpockget = self.dic.get('5')
        self.ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
        self.lbl_Lagarto = Label(raiz, image=valorLagartoget, background="dimgray").place(x=250, y=300)
        self.lbl_LagartoRandom = Label(raiz, image=self.ImagenRandom, background="dimgray").place(x=1150, y=300)
        if self.ImagenRandom == valorLagartoget:
            self.empate()
        elif self.ImagenRandom == valorSpockget:
            self.ganas()
        elif self.ImagenRandom == valorPapelget:
            self.ganas()
        elif self.ImagenRandom == valorTijeraget:
            self.pierdes()
        elif self.ImagenRandom == valorPiedraget:
            self.pierdes()

    def btnspock(self, raiz):
        self.raiz = raiz
        self.dic = {'1': PhotoImage(file="img/Piedra.png"), '2': PhotoImage(file="img/Papel.png"),
               '3': PhotoImage(file="img/Tijeras.png"), '4': PhotoImage(file="img/Lagarto.png"),
               '5': PhotoImage(file="img/Spock.png")}
        valorPiedraget = self.dic.get('1')
        valorPapelget = self.dic.get('2')
        valorTijeraget = self.dic.get('3')
        valorLagartoget = self.dic.get('4')
        valorSpockget = self.dic.get('5')
        self.ImagenRandom = random.choice([valorPiedraget, valorPapelget, valorTijeraget, valorLagartoget, valorSpockget])
        self.lbl_Spock = Label(raiz, image=valorSpockget, background="dimgray").place(x=250, y=300)
        self.lbl_SpockRandom = Label(raiz, image=self.ImagenRandom, background="dimgray").place(x=1150, y=300)
        if self.ImagenRandom == valorSpockget:
            self.ganas()
        elif self.ImagenRandom == valorTijeraget:
            self.ganas()
        elif self.ImagenRandom == valorPiedraget:
            self.ganas()
        elif self.ImagenRandom == valorLagartoget:
            self.pierdes()
        elif self.ImagenRandom == valorPapelget:
            self.pierdes()
