islem = input("İşlem Seçiniz (+, -, *, /): ")
s1 = float(input("1. Sayıyı giriniz: "))
s2 = float(input("2. Sayıyı giriniz: "))
if islem == "+":
    top = s1 + s2
    print(f"{s1} + {s2} = {top}")
elif islem == "-":
    top = s1 - s2
    print(f"{s1} - {s2} = {top}")
if islem == "*":
    top = s1 * s2
    print(f"{s1} x {s2} = {top}")
if islem == "/":
    top = s1 / s2
    print(f"{s1} / {s2} = {top}")
