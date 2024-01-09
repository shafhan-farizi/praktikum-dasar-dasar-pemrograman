# 1. Fungsi untuk menampilkan data diri
def profil(nama, alamat, gender, umur, hoby):
    print("Nama : ", nama)
    print("Alamat : ", alamat)
    print("Gender : ", gender)
    print("Umur : ", umur)
    print("Hoby : ", hoby)

profil("Shafhan Farizi", "Jln. Kukusan Beji", "Laki-Laki", 19, "Memecahkan masalah\n")

# 2. Fungsi untuk mencari kelulusan berdasarkan nilai
def nilai(nilai):
    if 0 <= nilai <= 60:
        keterangan = "Gagal"
    elif 60 < nilai <= 70:
        keterangan = "Baik"
    elif 70 < nilai <= 80:
        keterangan = "Sangat Baik"
    elif 80 < nilai <= 100:
        keterangan = "Istimewa"
    else:
        print("Masukkan nilai yang benar Bruh!")
        exit()
    print("Keterangan kelulusan : ", keterangan, "\n")

nilai(100)

# 3. Fungsi untuk mencetak nilai bilangan ganjil dari parameter yang dimasukkan
def ganjil(angka):
    if isinstance(angka, int):
        for i in range(angka+1):
            if i % 2 != 0:
                print(i)
    else:
        print("Masukkan angka Bruh!")
        exit()
ganjil(99)