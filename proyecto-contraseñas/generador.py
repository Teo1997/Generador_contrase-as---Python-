import random

def generar_password():
    mayusculas = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "X", "Z" ]
    minusculas = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "x", "z" ]
    simbolos = ["!", "#", "$", "%", "&", "/", "?"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        caracter_aleatorio = random.choice(caracteres)
        password.append(caracter_aleatorio)

    password = "".join(password) # genera un string de la lista original
    return password


def run():
    password = generar_password()
    print("Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()