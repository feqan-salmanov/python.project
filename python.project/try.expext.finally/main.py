x=float(input("no 1:"))
y=float(input("no 2:"))
try:
    print("cavabiniz:", x / y)
except ZeroDivisionError:
    print("hatali sayi")
finally:
    print("islem bitti")
