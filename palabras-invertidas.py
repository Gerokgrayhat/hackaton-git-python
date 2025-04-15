def es_palindromo(palabra):
    
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def main():
    palabra = input("Ingrese una palabra o frase: ")
    if es_palindromo(palabra):
        print(f"La palabra/frase '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra/frase '{palabra}' no es un palíndromo.")

if __name__ == "__main__":
    main()
