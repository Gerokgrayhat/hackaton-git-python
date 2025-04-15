def es_palindromo(palabra):
    # Normaliza la palabra: elimina espacios y convierte a minúsculas
    palabra = palabra.replace(" ", "").lower()
    # Compara la palabra con su reverso
    return palabra == palabra[::-1]

def main():
    palabra = input("Ingrese una palabra o frase: ")
    if es_palindromo(palabra):
        print(f"La palabra/frase '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra/frase '{palabra}' no es un palíndromo.")

if __name__ == "__main__":
    main()
