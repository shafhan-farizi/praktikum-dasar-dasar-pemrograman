class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class Onta(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jumlah_kaki, kemampuan_khusus):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jumlah_kaki = jumlah_kaki
        self.kemampuan_khusus = kemampuan_khusus

    def minumBanyak(self, liter):
        print(f'{self.name} meminum sebanyak {liter} liter')
    
    def makanBanyak(self, kilo):
        print(f'{self.name} memakan sebanyak {kilo}kg')
    
class Kucing(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, suara, kebiasaan):
        super().__init__(name, makanan, hidup, berkembang_biak) 
        self.suara = suara
        self.kebiasaan = kebiasaan

    def miaw(self):
        print(f'{self.name} melakukan {self.suara}')

    def menggaruk(self, sesuatu):
        print(f'{self.name} sedang menggaruk {sesuatu}')

class Cacing(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang, warna_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.warna_kulit = warna_kulit

    def makan(self, makanan):
        print(f'{self.name} sedang memakan {makanan}')

    def mati(self, penyebab):
        print(f'{self.name} mati disebabkan {penyebab}')

class Dinosaurus(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, tinggi, berat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.tinggi = tinggi
        self.berat = berat

    def makan(self, makanan):
        print(f'{self.name} memakan {makanan}')
    
    def hancurkan(self, nama_tempat):
        print(f'{self.name} menghancurkan tempat {nama_tempat}')

class Angsa(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kecepatan, umur):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.kecepatan = kecepatan
        self.umur = umur

    def kejar(self, target):
        print(f'{self.name} sedang mengejar {target}')

    def terbang(self, jarak):
        print(f'{self.name} terbang sejauh {jarak}km')
        
print('Onta')
onta = Onta('Onta', 'herbivora', 'darat', 'vivipar', 4, 'dapat bertahan di gurun dalam waktu lama')
onta.minumBanyak(5)
onta.makanBanyak(100)
print('')

print('Kucing')
kucing = Kucing('Kucing', 'karnivora', 'darat', 'vivipar', 'miau', 'tidur dan makan')
kucing.miaw()
kucing.menggaruk('karpet')
print('')

print('Cacing')
cacing = Cacing('Cacing', 'herbivora', 'tanah', 'ovipar', 2, 'pink')
cacing.makan('bakteri')
cacing.mati('memakan garam')
print('')

print('Dinosaurus')
dinosaurus = Dinosaurus('Dinosaurus', 'omnivora', 'darat', 'ovipar', 100, 250)
dinosaurus.hancurkan('stasiun pondok cina')
dinosaurus.makan('setengah manusia')
print('')

print('Angsa')
angsa = Angsa('Soang', 'herbivora', 'amfibi', 'ovipar', 5, 5)
angsa.kejar('Wozazki')
angsa.terbang(15)