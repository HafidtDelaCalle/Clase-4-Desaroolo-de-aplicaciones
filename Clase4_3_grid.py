import tkinter as tk

# Crear la ventana 
ventana = tk.Tk()
ventana.title('Ventana de ejemplo')
ventana.geometry('500x200')

lb1=tk.Label(ventana, text='Ingresar Numero 1')
lb1.grid(row=0,column=0)

num1 = tk.Entry(ventana)
num1.grid(row=0, column=1, pady=5, padx=10)

lb2=tk.Label(ventana, text='Ingresar Numero 2')
lb2.grid(row=1,column=0)


num2 = tk.Entry(ventana)
num2.grid(row=1, column=1, pady=5, padx=10)

#Label  y caja de texto para resultado
lb3=tk.Label(ventana, text='El resultado es:')
lb3.grid(row=2,column=0,padx=25)

res = tk.Entry(ventana)
res.grid(row=2, column=1, pady=5, padx=10)

# Bloque de botones
btnsuma=tk.Button(ventana, text='+')
btnsuma.grid(row=0, column=2,padx=5)

btnresta = tk.Button(ventana, text='-')
btnresta.grid(row=0,column=3,padx=5)

btnmulti = tk.Button(ventana, text='*')
btnmulti.grid(row=1,column=2,padx=5)

btndiv = tk.Button(ventana, text='/')
btndiv.grid(row=1,column=3,padx=5)

ventana.mainloop()
