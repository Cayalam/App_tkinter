#Se importa libreria tkinter con todas sus funciones

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
# funciones de la app

def invertir():
    messagebox.showinfo("Inertir 1.0", "Hizo clic en el boton invertir...")
    x4=(int(x.get()))%10
    x3=((int(x.get()))%100)//10
    x2=((int(x.get()))%1000)//100
    x1=((int(x.get()))-(int(x.get()))%1000)//1000
    
    t_resultados.insert(INSERT, "El numero invertido, probablemente es: "+str(x4) + str(x3)+ str(x2)+ str(x1))

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    x.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

# variables globales 


#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Invertidor de numeros")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")

x = StringVar()

#--------------------
#frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "sky blue", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)





# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "Inertir numero de 4 digitos al revés")
titulo.config(bg = "sky blue", fg = "slate gray", font = ("ALGERIAN",16))
titulo.place(x = 32, y = 20)

# Etiqueta para x
lb_x = Label(frame_entrada, text = "X = ")
lb_x.config(bg="sky blue", fg="dark slate gray", font=("Arial Black",20))
lb_x.place(x=115, y=120, width=115, height=30)


# Entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial Black",20), justify=LEFT,fg="dark slate gray")
entry_x.focus_set()
entry_x.place(x=195, y=120, width=115, height=30)  

#--------------------
#frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "sky blue", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 260)


# Boton para Invertir Numero
fotoinvertir = PhotoImage(file="descarga.png")
bt_invertir = Button(frame_operaciones, text="Invertir", image=fotoinvertir,command=invertir)
bt_invertir.place(x=45, y=45, width=100, height=30)

#Boton borrar
bt_borrar = Button(frame_operaciones, text="Borrar")
bt_borrar.place(x=190, y=45, width=100, height=30)



#Boton borrar
bt_borrar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_borrar.place(x=190, y=45, width=100, height=30)

# Boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="sky blue", width=480, height=100)
frame_resultados.place(x=10, y = 390)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="Khaki4", fg="black", font=("Arial Black",18))
t_resultados.place(x=10,y=10, width=460, height= 80)

ventana_principal.mainloop()