import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

# Parametry wejściowe
initial_price = 120_000
annual_growth_rate = 0.05
years = 5
months = years * 12

# Cena mieszkania po 5 latach
future_price = initial_price * (1 + annual_growth_rate) ** years
print(f"Orientacyjna cena mieszkania za 5 lat: {future_price:.2f} zł")

# Parametry lokaty
annual_interest_rate = 0.12
monthly_interest_rate = annual_interest_rate / 12

# Miesięczna wpłata
monthly_payment = -npf.pmt(rate=monthly_interest_rate, nper=months, pv=0, fv=future_price, when='end')
print(f"Potrzebna miesięczna wpłata: {monthly_payment:.2f} zł")

months_array = np.arange(months + 1)

housing_price_timeline = initial_price * (1 + annual_growth_rate / 12) ** months_array

deposit_timeline = np.zeros(months + 1)
for i in range(1, months + 1):
    deposit_timeline[i] = deposit_timeline[i-1] * (1 + monthly_interest_rate) + monthly_payment

plt.plot(months_array, housing_price_timeline, label="Cena mieszkania")
plt.plot(months_array, deposit_timeline, label="Wartość lokaty")
plt.xlabel("Miesiące")
plt.ylabel("Wartość [zł]")
plt.legend()
plt.grid(True)