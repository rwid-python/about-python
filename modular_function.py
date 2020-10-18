# Introducing Function at Python.
# Declare function use def


def calc2(tipe, var1, var2):
    if tipe == '+':
        hasil = var1 + var2
    elif tipe == '-':
        hasil = var1 - var2
    elif tipe == 'x':
        hasil = var1 * var2
    elif tipe == ':':
        hasil = var1 / var2
    return hasil


def hitung_luas(tipe, var1, var2):
    if tipe == 'persegi':
        luas = var1 * var2
    elif tipe == 'segitiga':
        luas = var1 * var2 / 2
    return luas


print(f"Calculator Result : {calc2(':', 1, 2)}")
v1 = 10
v2 = 20
print({hitung_luas('persegi',v1,v2)})
print(f"Calculate Area "
      f"\n 1. Square use length {v1} ; width {v2} = {hitung_luas('persegi',v1,v2)}"
      f"\n 2. Triangle use base {v1} ; high {v2} = {hitung_luas('segitiga',v1,v2)} ")
