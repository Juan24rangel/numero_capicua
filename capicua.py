
from tkinter import *
from tkinter import messagebox
from math import trunc

# funciones de la app

def comp():
    messagebox.showinfo("Comp 1.0", "Se esta comprobando...")
    z = int(x.get())

    C1 = trunc (z/10000)
    R1 = z % 10000
    C2 = trunc (R1/1000)
    R2 = R1 % 1000
    C3 = trunc (R2/100)
    R3 = R2 %100
    C4 = trunc (R3/10)
    C5 = R3 % 10
    if C5==C1:
        y = ("si es capicua")
    else:
        if C5!=C1:
            y = ("no es capicua")
    if C4==C2:
        y = ("si es capicua")
    else:
        if C4!=C2:
            y = ("no es capicua")
    t_resultados.insert(INSERT, "El numero " + x.get()+ " , "+str(y)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados.")
    x.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara.")
    ventana_principal.destroy()

# variables globales 


#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Sistemas UIS")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="midnight blue")

x = StringVar()

#--------------------
#frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "skyblue2", width = 480 , height = 200)
frame_entrada.place(x = 10, y = 10)

# Logo de la app
#logo = PhotoImage(file = "img/logo-uis.png")
#lb_logo = Label(frame_entrada, image = logo)
#lb_logo.place(x = 61 , y = 61)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "Comprobar si un numero es capicua")
titulo.config(bg = "skyblue2", fg = "black", font = ("Arial",16))
titulo.place(x = 60, y = 10)

# Etiqueta para x
lb_x = Label(frame_entrada, text = "X = ")
lb_x.config(bg="skyblue2", fg="black", font=("Arial",16))
lb_x.place(x=10, y=100, width=115, height=30)

# Entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial",20), justify=LEFT,fg="black")
entry_x.focus_set()
entry_x.place(x=85, y=100, width=115, height=30)

#--------------------
#frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "skyblue2", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 220)

# Boton para sumar
bt_sumar = Button(frame_operaciones, text="Comprobar", command=comp)
bt_sumar.place(x=45, y=45, width=100, height=30)

#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar")
bt_sumar.place(x=190, y=45, width=100, height=30)


#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_sumar.place(x=190, y=45, width=100, height=30)

# Boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="skyblue1", width=480, height=140)
frame_resultados.place(x=10, y = 350)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="lightsteelblue1", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=460, height= 120)

ventana_principal.mainloop()