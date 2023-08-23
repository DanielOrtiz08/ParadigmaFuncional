import tkinter as tk
from math import isqrt

# Definimos una función lambda llamada 'es_primo' que toma un argumento 'n'
# para determinar si un número es primo
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, isqrt(n) + 1))

# Función que genera una lista de números primos en un rango dado
def find_primes_in_range(start, end):
    return list(filter(is_prime, range(start, end + 1)))

# Función para mostrar los números primos en una etiqueta de la GUI
def display_primes_in_gui():
    start = int(entry_start.get())
    end = int(entry_end.get())
    
    primes = find_primes_in_range(start, end)
    result_label.config(text=f"\nNúmeros primos encontrados:\n {', '.join(map(str, primes))}")

# Crear la ventana de la aplicación
app = tk.Tk()
app.title("Encontrar Números Primos")

# Etiquetas e input para el rango
label_start = tk.Label(app, text="Ingrese el número de inicio del rango:")
label_start.pack()
entry_start = tk.Entry(app)
entry_start.pack()

label_end = tk.Label(app, text="Ingrese el número final del rango:")
label_end.pack()
entry_end = tk.Entry(app)
entry_end.pack()

# Botón para encontrar números primos
find_button = tk.Button(app, text="Encontrar Números Primos", command=display_primes_in_gui)
find_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(app, text="")
result_label.pack()

# Iniciar la aplicación
app.mainloop()
