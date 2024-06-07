def valor_letra(letra):
    """Devuelve el valor de una letra minúscula según su posición en el alfabeto."""
    return ord(letra) - ord('a') + 1

def validar_cadena(cadena):
    """Verifica si la cadena contiene solo letras minúsculas."""
    for i, c in enumerate(cadena):
        if not c.islower():
            if c.isupper():
                return False, f"Cambia a minúscula la letra '{c}' en la posición {i + 1}."
            elif c.isdigit():
                return False, f"Cambia el número en la posición {i + 1} por una letra minúscula."
    return True, ""

def suma_valores_cadena(cadena):
    """Calcula la suma de los valores de las letras en la cadena."""
    return sum(valor_letra(c) for c in cadena)

def main():
    while True:
        cadena = input("Introduce una cadena de letras minúsculas: ")
        es_valida, mensaje = validar_cadena(cadena)
        
        if es_valida:
            suma = suma_valores_cadena(cadena)
            print(f"La suma de los valores de las letras en la cadena es: {suma}")
            break
        else:
            print(mensaje)

if __name__ == "__main__":
    main()