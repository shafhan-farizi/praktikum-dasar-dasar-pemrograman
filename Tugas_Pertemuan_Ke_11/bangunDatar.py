def keliling_segitiga(sisiA, sisiB, sisiC):
    hasil = sisiA + sisiB + sisiC
    return hasil

def luas_segitiga(alas, tinggi):
    hasil = (alas * tinggi) / 2
    return hasil

def keliling_persegi(sisi):
    hasil = 4 * sisi
    return hasil

def luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil

def keliling_persegi_panjang(panjang, lebar):
    hasil = (2 * panjang) + (2 * lebar)
    return hasil

def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil

def keliling_belah_ketupat(sisi):
    hasil = 4 * sisi
    return hasil

def luas_belah_ketupat(diagonal1, diagonal2):
    hasil = (diagonal1 * diagonal2) / 2
    return hasil

def keliling_jajar_genjang(sisiA, sisiB):
    hasil = 2 * (sisiA + sisiB)
    return hasil

def luas_jajar_genjang(alas, tinggi):
    hasil = alas * tinggi
    return hasil

def keliling_trapesium(sisiA, sisiB, sisiC, sisiD):
    hasil = sisiA + sisiB + sisiC + sisiD
    return hasil

def luas_trapesium(sisiA, sisiB, tinggi):
    hasil = ((sisiA + sisiB) * tinggi) / 2
    return hasil

def keliling_lingkaran(radius):
    if radius % 7 != 0:
        phi = 22/7
    else:
        phi = 3.14
    hasil = 2 * phi * radius
    return round(hasil, 2)

def luas_lingkaran(radius):
    if radius % 7 != 0:
        phi = 22/7
    else:
        phi = 3.14
    hasil = phi * radius * radius
    return round(hasil, 2)
