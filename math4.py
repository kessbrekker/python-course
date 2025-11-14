# Çemberin çevresi ve alanını hesaplama

import math

cap = float(input("Çemberin Çapını giriniz : "))

yaricap = cap/2

cevre = 2 * (math.pi * (yaricap))
alan = math.pi * pow(yaricap, 2)

print(f"Çevresi : {round(cevre, 2)} \nAlanı : {round(alan, 2)}")