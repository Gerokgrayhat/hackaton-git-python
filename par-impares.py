def verificar_pares_impares():
    numeros = list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
