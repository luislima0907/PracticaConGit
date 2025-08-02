from calculator import Calculator

def main():
    calc = Calculator()
    while True:
        print("Seleccione la operación:")
        print("1. Sumar")
        print("6. Salir")

        choice = input("Ingrese su elección (1-6): ")

        if choice == '6':
            print("Saliendo de la calculadora.")
            break
        
        if choice in ['1']:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            if choice == '1':
                print(f"Resultado: {calc.add(a, b)}")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()