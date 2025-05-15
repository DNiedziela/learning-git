import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calcnewfile.log")

def pobierz_dane():

    operacja = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    if operacja not in ["1", "2", "3", "4"]:
        print("Niepoprawna wartość w polu 'działanie' ")
        logging.info("Użytkownik wybrał liczbę spoza zakresu")
        sys.exit()
    
    pierwsza = float(input("Podaj pierwszą liczbę: "))
    druga = float(input("Podaj drugą liczbę: "))

    return operacja, pierwsza, druga

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

def kalkulator():
    operacja, a, b = pobierz_dane()

    operacje = {
        "1": dodawanie,
        "2": odejmowanie,
        "3": mnozenie,
        "4": dzielenie
    }

    funkcja = operacje[operacja]
    wynik = funkcja(a, b)
    print(f"Wynik: {wynik}")
    logging.info(f"Użytkownik wybrał {operacja} na liczbach {a} i {b}")

if __name__ == "__main__":
    kalkulator()
