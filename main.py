numbers = range(101)

podzielne = []
spotegowane = []

for i in numbers:
    if i % 7 == 0:
        podzielne.append(i)
     
for i in podzielne:
    spotegowane.append(i ** 3)


print(podzielne)
print(spotegowane)