import tkinter as tk
from tkinter import messagebox

# Crear la funcion mostrar_mensaje
def mostrar_mensaje():
    mensaje = caja_texto.get() # atrapar el valor de la caja de texto
    messagebox.showinfo('Mensaje', f"Has ingresado el texto: {mensaje}") # imporimir la varianle

# crear la ventana
ventana = tk.Tk() # configuracion interna de la libreria para indicar que es una ventana
ventana.title("Mi primera ventana") # agregar un titulo 
ventana.geometry('500x200') # tamaño de la ventana
# ventana.attributes('-fullscreen', True)

# Crear una caja de texto
caja_texto =tk.Entry(ventana) # relaciono con la interfaz
caja_texto.pack(pady=10) # Muestra la caje de texto en la interfaz

# Crear un boton
boton = tk.Button(ventana,text='Aceptar',command=mostrar_mensaje) # relaciono con la interfase
boton.pack()# desplegar


# Visualizar la ventana
ventana.mainloop() # Muestra la ventana y la mantiene abierta hasta que el usuarui la cierra

