import tkinter as tk
from tkinter import messagebox
from generator import generate_password

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Generador de Contraseñas")
    ventana.geometry("420x400")

    tk.Label(
        ventana,
        text="Generador de Contraseñas"
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        ventana,
        text="Longitud de la Contraseña"
    ).pack()

    entry_longitud = tk.Entry(
        ventana,
        width=10,
        justify="center"
    )

    entry_longitud.insert.BooleanVar(value=True)
    entry_longitud.pack(pady=8)

    var_mayusculas = tk.BooleanVar(value=True)
    var_minusculas = tk.BooleanVar(value=True)
    var_numeros= tk.BooleanVar(value=True)
    var_simbolos= tk.BooleanVar(value=True)

    tk.CheckButton(
        ventana,
        text="Mayúsculas (A-Z)"
        variable=var_mayusculas
    ).pack()

    tk.CheckButton(
        ventana,
        text="Minúsculas (a-z)"
        variable=var_minusculas
    ).pack()

    tk.CheckButton(
        ventana,
        text="Números (0-9)"
        variable=var_numeros
    ).pack()

    tk.CheckButton(
        ventana,
        text="Símbolos (!@#$...)"
        variable=var_simbolos
    ).pack()

    entry_resultado.pack(pady=15)

    def generar():
        try:
            longitud=int(entry_longitud.get())

            if longitud < 4:
                messagebox.showwarning(
                    "Error",
                    "La longitud minima es 4."
                )
                return

            password = generate_password(
                longitud,
                var_mayusculas.get(),
                
            )