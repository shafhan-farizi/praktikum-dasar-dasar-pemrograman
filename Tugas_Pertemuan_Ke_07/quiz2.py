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