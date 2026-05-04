"""
Desarrollo de Binomios de Newton
--------------------------------
Autor: Zoe Solis
Materia: Matemática Discreta
Descripción: Programa para desarrollar y simplificar binomios del tipo (a + b)^n
utilizando el Teorema del Binomio y combinatoria.
"""

# ---------------------------------------------------------
# FUNCIONES MATEMÁTICAS (Lógica de Discreta)
# ---------------------------------------------------------

def calcular_factorial(n):
    """Calcula el factorial de un número n!"""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def combinatoria(n, k):
    """Calcula el coeficiente binomial C(n, k)"""
    return calcular_factorial(n) // (calcular_factorial(k) * calcular_factorial(n - k))


# ---------------------------------------------------------
# PROCESAMIENTO DE TÉRMINOS Y VARIABLES
# ---------------------------------------------------------

def separar_coeficiente_y_variables(texto):
    """Separa el coeficiente numérico de las letras (ej: '-4xy' -> -4, 'xy')"""
    texto = texto.strip()
    if texto == "":
        return 1, ""

    signo = -1 if texto.startswith("-") else 1
    if texto[0] in "+-":
        texto = texto[1:]

    numero = ""
    letras = ""

    for caracter in texto:
        if caracter.isdigit():
            numero += caracter
        elif caracter.isalpha():
            letras += caracter

    coef = int(numero) if numero else 1
    return signo * coef, letras

def simplificar_variables(letras):
    """Simplifica variables repetidas (ej: 'xxy' -> 'x^2y')"""
    cuenta = {}
    for letra in letras:
        cuenta[letra] = cuenta.get(letra, 0) + 1

    resultado = ""
    for letra in sorted(cuenta):
        cantidad = cuenta[letra]
        if cantidad == 1:
            resultado += letra
        else:
            resultado += f"{letra}^{cantidad}"
    return resultado

def construir_termino(coef, letra1, exp1, letra2, exp2):
    """Arma un término final con sus potencias correspondientes"""
    letras = ""
    if exp1 > 0:
        letras += letra1 * exp1
    if exp2 > 0:
        letras += letra2 * exp2

    if letras == "":
        return str(coef)

    # Si el coeficiente es 1 o -1, manejamos la estética
    prefijo = ""
    if coef == -1:
        prefijo = "-"
    elif coef != 1:
        prefijo = str(coef)

    return prefijo + simplificar_variables(letras)


# ---------------------------------------------------------
# LÓGICA DE DESARROLLO Y SALIDA
# ---------------------------------------------------------

def mostrar_como_expresion(lista):
    """Une los términos en una cadena legible con signos + y -"""
    resultado = ""
    for i, t in enumerate(lista):
        if t.startswith("-"):
            resultado += " - " + t[1:]
        else:
            if i == 0:
                resultado += t
            else:
                resultado += " + " + t
    return resultado

def desarrollar_binomio(a_texto, b_texto, exponente):
    """Realiza el desarrollo completo del binomio de Newton"""
    a_coef, a_vars = separar_coeficiente_y_variables(a_texto)
    b_coef, b_vars = separar_coeficiente_y_variables(b_texto)

    print(f"\nExpresión: ({a_texto} + {b_texto})^{exponente}")
    print("-" * 30)

    terminos = []
    resumen = {}

    for k in range(exponente + 1):
        c = combinatoria(exponente, k)
        coef_final = c * (a_coef ** (exponente - k)) * (b_coef ** k)
        exp_a = exponente - k
        exp_b = k

        termino = construir_termino(coef_final, a_vars, exp_a, b_vars, exp_b)
        terminos.append(termino)

        # Agrupar para simplificación
        letras_temp = (a_vars * exp_a) + (b_vars * exp_b)
        clave = simplificar_variables(letras_temp) if letras_temp else "constante"
        resumen[clave] = resumen.get(clave, 0) + coef_final

    print("\nDesarrollo paso a paso:")
    print(mostrar_como_expresion(terminos))

    # Forma simplificada final
    print("\nForma simplificada:")
    final = []
    for clave, valor in resumen.items():
        if valor == 0: continue
        if clave == "constante":
            final.append(str(valor))
        else:
            if valor == 1: final.append(clave)
            elif valor == -1: final.append("-" + clave)
            else: final.append(f"{valor}{clave}")

    print(mostrar_como_expresion(final))


# ---------------------------------------------------------
# INTERFAZ DE USUARIO (Punto de entrada)
# ---------------------------------------------------------

def main():
    print("========================================")
    print(" CALCULADORA DE BINOMIO DE NEWTON ")
    print("========================================\n")

    # Validación de entradas
    while True:
        a = input("Ingresá el primer término (ej: x, 2xy, -3):\n> ").strip()
        if a: break
        print("Error: no puede estar vacío.")

    while True:
        b = input("Ingresá el segundo término (ej: y, 5, -z):\n> ").strip()
        if b: break
        print("Error: no puede estar vacío.")

    while True:
        n_str = input("Ingresá el exponente (n ≥ 0):\n> ").strip()
        if n_str.isdigit():
            n = int(n_str)
            break
        print("Error: debe ser un número entero no negativo.")

    desarrollar_binomio(a, b, n)
    print("\n" + "=" * 40)

if __name__ == "__main__":
    main()
