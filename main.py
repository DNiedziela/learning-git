numbers = range(101)

podzielne = []
spotegowane = []
# tworzenie zakresu i list liczb

for i in numbers:
    if i % 7 == 0:
        podzielne.append(i)
     
for i in podzielne:
    spotegowane.append(i ** 3)
#petle wykluczająca liczby niepasujące do warunków

print(podzielne)
print(spotegowane)
# drukuje obie liczby

# kolejny commit dla obycia
