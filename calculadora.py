def calculadora():
    while True:
        operacion = input("Ingrese la operación (+, -, *, /) o 'salir' para terminar: ")
        if operacion == 'salir':
            break
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if operacion == '/':
            if num2 == 0:
                print("Error: División por cero")
                continue
        # Realizar la operación
        if operacion == '+':
            print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
            print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
            print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
            print(f"Resultado: {num1 / num2}")
        else:
            print("Operación no válida")
