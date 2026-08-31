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
    )

    tk.CheckButton(
        ventana,
        text="Minúsculas (a-z)"
        variable=var_minusculas
    )

    tk.CheckButton(
        ventana,
        text="Números (0-9)"
        variable=var_numeros
    )

    tk.CheckButton(
        ventana,
        text="Símbolos (!@#$...)"
        variable=var_mayusculas
    )