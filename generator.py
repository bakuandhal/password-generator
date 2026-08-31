import secrets
import string

def generate_password (longitud, mayusculas, minusculas, numeros, simbolos):
    caracteres = ""

    if minusculas: 
        caracteres += string.ascii_lowercase

    if mayusculas:
        caracteres += string.ascii_uppercase

    if numeros:
        caracteres += string.digits

    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Selecciona al menos una opción"

    password = ""

    for _ in range(longitud):
        password += secrets.choice(caracteres)

    return password


resultado = generate_password(
        12,
        True,
        True,
        True,
        True
)

print(resultado)


