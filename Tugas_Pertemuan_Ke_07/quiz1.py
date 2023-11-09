# QUIZ1
nama_kendaraan = input("Nama kendaraan (mobil/motor): ")

print('Pilihan jenis bensin: ')
print('1. Pertalite')
print('2. Pertamax')
print('3. Pertamax Turbo\n')

jenis_bensin = int(input("Jenis Bensin : "))
print("\n")

match jenis_bensin:
    case 1:
        jenis_bensin = 'Pertalite'
        harga = 10000
        jarak_tempuh = 12
    case 2:
        jenis_bensin = 'Pertamax'
        harga = 14000
        jarak_tempuh = 13
    case 3:
        jenis_bensin = 'Pertamax Turbo'
        harga = 17000
        jarak_tempuh = 13.5
    case _:
        print('Pilih yang benar')
        exit()

print('Pilihan kota tujuan: ')
print('1. Jakarta')
print('2. Bekasi')
print('3. Depok')
print('4. Tangerang')
print('5. Bogor\n')

kota_tujuan = int(input('Kota tujuan : '))
match kota_tujuan:
    case 1:
        kota = 'Jakarta'
        jarak = 20
    case 2:
        kota = 'Bekasi'
        jarak = 35.7
    case 3:
        kota = 'Depok'
        jarak = 5
    case 4: 
        kota = 'Tangerang'
        jarak = 99
    case 5:
        kota = 'Bogor'
        jarak: 120.6
    case _:
        print('Pilih yang benar')
        exit()

pemakaian_bensin = round(jarak_tempuh / jarak, 2)
print('Output: ')
print(f"Nama kendaraan : {nama_kendaraan}")
print(f"Jenis bensin : {jenis_bensin}")
print(f"Kota yang dituju : {kota}")
print(f"Pemakaian bensin : {pemakaian_bensin}")
print(f"Total harga dari bensin : {pemakaian_bensin * harga}")

# QUIZ2
nama_pembeli = input('Nama pembeli: ')

no_hp = input('No HP pembeli: ')

pesan_apa = input('Pesan menu apa (makanan/minuman): ')
match pesan_apa:
    case 'makanan':
        print('Pilihan menu makanan: ')
        print('1. Nasi Goreng Rp.15.000')
        print('2. Mie Goreng Rp.12.000')
        print('3. Ayam Geprek Rp.18.000')

        pilih_makan = int(input('Pilih menu makanan: '))
        match pilih_makan:
            case 1:
                nama_menu = 'Nasi Goreng'
                harga = 15000
            case 2:
                nama_menu = 'Mie Goreng'
                harga = 12000
            case 3:
                nama_menu = 'Ayam Geprek'
                harga = 18000
            case _:
                print('Pilih yang benar')
                exit()
    case 'minuman':
        print('Pilihan menu minuman: ')
        print('1. Aneka Jus Rp.15.000')
        print('2. Soft Drink Rp.10.000')
        print('3. Sweet Ice Tea Rp.5.000')

        pilih_makan = int(input('Pilih menu minuman: '))
        match pilih_makan:
            case 1:
                nama_menu = 'Aneka Jus'
                harga = 15000
            case 2:
                nama_menu = 'Soft Drink'
                harga = 10000
            case 3:
                nama_menu = 'Sweet Ice Tea'
                harga = 5000
            case _:
                print('Pilih yang benar')
                exit()
jumlah_pesanan = int(input('Jumlah pesanan: '))

print('Output: ')
print(f'Nama pembeli : {nama_pembeli}')
print(f'No HP pembeli: {no_hp}')
print(f'Menu yang dipesan: {nama_menu}')
print(f'Jumlah pesanan: {jumlah_pesanan}')
print(f'Harga yang harus dibayarkan: {harga*jumlah_pesanan}')

# QUIZ 3
for i in range(1, 21):
    if i % 3 == 0:
        print('STT Nurul Fikri')
    else:
        print(i)