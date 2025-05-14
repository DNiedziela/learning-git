import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calcfile.log")

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
        print("Niepoprawna wartość w polu 'działanie' ")
        sys.exit()
        
if __name__ == "__main__":
    a = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    b = float(input("Podaj pierwszą liczbę: "))
    c = float(input("Podaj drugą liczbę: "))

    logging.info(f"Użytkownik wybrał działanie {a} na liczbach {b} i {c}")
    print(f"Liczę {b} i {c}")
    print("Wynik to:", operation(a, b, c))