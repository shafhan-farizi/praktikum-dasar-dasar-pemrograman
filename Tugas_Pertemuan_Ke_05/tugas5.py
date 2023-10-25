# TUGAS 1
kendaraan = ['Avanza', 'Mobil', 1500, 'Silver', 4]
kendaraan.append('200jt')
kendaraan.append('MPV')
kendaraan.insert(2, 'Toyota')

print(kendaraan)

#TUGAS 2
print('Pilih antara 1 - 3\n1 = Persegi\n2 = Lingkaran\n3 = Segitiga\n')
JenisBangunDatar = int(input('Masukkan pilihanmu: '))
match JenisBangunDatar:
    case 1:
        sisi = int(input('Masukkan nilai untuk sisi:'))
        print(f'Luas persegi dengan sisi {sisi} adalah {sisi*sisi}')
    case 2:
        ruas = int(input('Masukkan nilai untuk ruas:'))
        if ruas % 7 == 0:
            phi = 22/7
        else:
            phi = 3,14
        print(f'Luas lingkaran dengan ruas {ruas} adalah {phi*ruas*ruas}')
    case 3:
        alas = int(input('Masukkan nilai untuk alas:'))
        tinggi = int(input('Masukkan nilai untuk tinggi:'))
        print(f'Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {alas*tinggi/2}')
    case _:
        print('Pilih hanya antara 1 - 3')