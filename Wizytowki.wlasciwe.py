from faker import Faker

fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.email}"

    def contact(self):
        return f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}"

    @property
    def label_length(self):
        return len(self.imie + self.nazwisko)

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, firma, stanowisko, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.firma = firma
        self.stanowisko = stanowisko
        self.telefon_sluzbowy = telefon_sluzbowy

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.stanowisko}, {self.firma}) - {self.email}"

    def contact(self):
        return f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}"

    @property
    def label_length(self):
        return len(self.imie + self.nazwisko)

def create_contacts(ilosc, typ):
    contacts = []

    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        if typ == "base":
            contact = BaseContact(imie, nazwisko, telefon, email)
        if typ == "business":
            firma = fake.company()
            stanowisko = fake.job()
            telefon_sluzbowy = fake.phone_number()
            contact = BusinessContact(imie, nazwisko, telefon, email, firma, stanowisko, telefon_sluzbowy)

        contacts.append(contact)

    return contacts

bazowe = create_contacts(2, "base")
biznesowe = create_contacts(2, "business")

print("BAZOWE WIZYTÓWKI:")
for kontakt in bazowe:
    print(kontakt)
    print(kontakt.contact())
    print(f"Długość: {kontakt.label_length}")
    print("---")

print("\nBIZNESOWE WIZYTÓWKI:")
for kontakt in biznesowe:
    print(kontakt)
    print(kontakt.contact())
    print(f"Długość: {kontakt.label_length}")
    print("---")
