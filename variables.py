name = "Kess"

a = 0.5
b = 0.1
c = a + b
print("Hello " + name + ": " + str(a) + " + " + str(b) + " = " + str(c))

# f-string method
print(f"Hello {name}: {a} + {b} = {c}")

print("-----------------------------------------------")

is_developer = True

if is_developer:
    dev_check = "Yes"
else:
    dev_check = "No"

print(f"Are you Developer? = {dev_check}")