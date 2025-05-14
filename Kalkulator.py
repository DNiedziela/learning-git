import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calc.log")

 
def operation(a, b, c):
    if a == 1:
        return b + c
    elif a == 2:
        return b - c
    elif a == 3:
        return b * c
    elif a == 4:
        return b / c
    else:
        print("Niepoprawna wartość")
        sys.exit()

if __name__ == "__main__":
    a = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    b = input("Podaj pierwszą liczbę: ")
    c = input("Podaj drugą liczbę: ")
    print(f"Liczę {sys.argv[2]} i {sys.argv[3]}")
    print(operation(a, b, c))