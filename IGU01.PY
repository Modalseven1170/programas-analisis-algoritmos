import tkinter as tk
import matplotlib.pyplot as plt
'''
#para instalar a libreria
pip install matplotilib
'''
x = [3, 4, 5, 6, 7]
y = [10, 11, 14, 16, 18]

plt.plot(x,y) #Grafica de linea
plt.scatter(x,y, colorizer="red") # grafica de puntos
#plt.bar(x,y) #Grafica de barras
plt.title("Mi primera grafica")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.show()

'''
def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre= "Bruno"
    lbl.config(text=f"hola, {nombre}"!!!)

root =tk.Tk()
root.title("saludador")
root.geometry("360x220")

lbl = tk.Label(root, text="Eh compa, escribe tu nombre y presiona el boton",background="yellow",foreground="black")
lbl.pack(pady=10)
entrada=tk.Entry(root,background="blue")
entrada.pack(pady=10)
bot= tk.Button(root, text="saludar")
bot.pack(pady=10)
'''
root.mainloop()