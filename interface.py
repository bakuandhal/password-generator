import tkinter as tk
from tkinter import messagebox
from generator import generate_password

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Generador de Contraseñas")
    ventana.geometry("420x400")

    tk.Label(
        ventana,
        text="Generador de Contraseñas",
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

    tk.Checkbutton(
        ventana,
        text="Mayúsculas (A-Z)",
        variable=var_mayusculas
    ).pack()


    tk.Checkbutton(
        ventana,
        text="Minúsculas (a-z)",
        variable=var_minusculas
    ).pack()

    tk.Checkbutton(
        ventana,
        text="Números (0-9)",
        variable=var_numeros
    ).pack()

    tk.Checkbutton(
        ventana,
        text="Simbolos (!@#$...)",
        variable=var_simbolos
    ).pack()


    entry_resultado = tk.Entry(
        ventana,
        width=35,
        justify="center"
    )
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
                var_minusculas.get(),
                var_numeros.get(),
                var_simbolos.get()
            )

            if password is None:
                messagebox.showwarning(
                    "Error",
                    "Selecciona al menos una opcion."
                )
                return

            entry_resultado.delete(0, tk.END)
            entry_resultado.insert(0, password)

        except ValueError:
            messagebox.showerror(
                "Error",
                "Introduce un numero valido"
            )
    def copiar():
        password = entry_resultado.get()

        if not password:
            messagebox.showwarning(
                "Error",
                "Primero genera una contraseña"
            )
            return

        ventana.clipboard_clear()
        ventana.clipboard_append(password)
        ventana.update()

        messagebox.showinfo(
            "Copiado"
            "Contra copiada al portapapeles"
        )

    tk.Button(
        ventana,
        text="Generar password",
        command=generar
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Copiar al portapapeles",
        command=generar
    ).pack(pady=5)

    ventana.mainloop()