# Fungsi menampilkan nama siswa yang lulus dengan nilai di atas 65
hasil_akhir = [
    {'nama': 'Ahmad Muhsin', 'nilai': 95},
    {'nama': 'Pepe the Frog', 'nilai': 100},
    {'nama': 'Arthur Fist', 'nilai': 25},
    {'nama': 'Drake', 'nilai': 50},
    {'nama': 'Hide the Pain Harold', 'nilai': 89},
    {'nama': 'Woman Yelling at a Cat', 'nilai': 2},
    {'nama': 'Distracted Boyfriend', 'nilai': 92},
]

def lulus_saja(names):
    mahasiswa_lulus = []
    for name in names:
        if name['nilai'] > 65:
            mahasiswa_lulus.append(name['nama'])
    print(mahasiswa_lulus)

lulus_saja(hasil_akhir)

# Fungsi menampilkan list buah-buahan namun dengan urutan terbalik
buah = ['pisang', 'mangga', 'jeruk', 'nanas', 'semangka', 'melon']
def balikan(fruits):
    buah_terbalik = []
    for fruit in fruits:
        buah_terbalik.insert(0, fruit)
    print(buah_terbalik)

balikan(buah)

# Fungsi duplikasi nama buah
def duplikasi(fruits):
    buah_duplikasi = []
    for fruit in fruits:
        buah_duplikasi += [fruit, fruit]
    print(buah_duplikasi)

duplikasi(buah)

# Fungsi mencetak string yang berisi konsonan
def printConsonant(strings):
    consonant = 'aiueo'
    stringNoConsonant = ''

    for string in strings:
        if string.lower() not in consonant and string != ' ':
            stringNoConsonant += string
    
    print(stringNoConsonant)

printConsonant('Nurul Fikri')