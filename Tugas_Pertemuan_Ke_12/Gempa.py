class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa di %s dengan skala %.2f tidak berasa\n" % (self.lokasi,self.skala))
        elif 2 <= self.skala <= 4:
            print("Dampak gempa di %s dengan skala %.2f membuat bangunan retak-retak\n" % (self.lokasi, self.skala))
        elif 4 < self.skala <= 6:
            print("Dampak gempa di %s dengan skala %.2f membuat bangunan roboh\n" % (self.lokasi, self.skala))
        else:
            print("Dampak gempa di %s dengan skala %.2f membuat bangunan roboh dan berpotensi tsunami\n" % (self.lokasi, self.skala))


