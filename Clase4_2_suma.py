import tkinter as tk # importar la luberia

def sumar():
    n1 = int(num1.get())
    n2 = int(num2.get())
    resultado.set(n1+n2)

#Crear la ventana
ventana = tk.Tk()
ventana.title('Ventana de ejemplo') # Titulo de la ventana
ventana.geometry('300x200') # tamaño de la ventana

# Crear la caja de texto
num1 = tk.Entry(ventana)
num1.pack(pady=5)
num2=tk.Entry(ventana)
num2.pack(pady=5)

# Crear variable global para el resultado
resultado = tk.StringVar() # configuracion de variable global

# crear cajada de texto para el resultado
caja_resultado = tk.Entry(ventana, textvariable=resultado) # Relacionar con la variable global
caja_resultado.pack(pady=10)

boton_suma = tk.Button(ventana, text='Suma', command=sumar)
boton_suma.pack(pady=15)

ventana.mainloop()