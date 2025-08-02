from calculator import Calculator

def main():
    calc = Calculator()
    while True:
        print("Seleccione la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Salir")

        choice = input("Ingrese su elección (1-6): ")

        if choice == '6':
            print("Saliendo de la calculadora.")
            break

        if choice in ['1', '2', '3', '4', '5']:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            if choice == '1':
                print(f"Resultado: {calc.add(a, b)}")
            elif choice == '2':
                print(f"Resultado: {calc.subtract(a, b)}")
            elif choice == '3':
                print(f"Resultado: {calc.multiply(a, b)}")
            elif choice == '4':
                print(f"Resultado: {calc.divide(a, b)}")
            elif choice == '5':
                print(f"Resultado: {calc.power(a, b)}")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()