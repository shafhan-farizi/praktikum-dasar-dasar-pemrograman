from tkinter import messagebox
import ttkbootstrap as ttk
import random

class Quiz:
    def __init__(self, root):
        self.soalQuiz = [
            {
                'soal': 'Apa nama ibukota Indonesia?',
                'pilihan': ['Jakarta', 'Bandung', 'Bogor', 'Padang'],
                'benar': 'Jakarta'
            },
            {
                'soal': 'Apa nama presiden Indonesia ke 7?',
                'pilihan': ['Megawati', 'Ganjar', 'Jokowi', 'Anies'],
                'benar': 'Jokowi'
            },
            {
                'soal': 'Senyawa air terdiri dari unsur-unsur...',
                'pilihan': ['H dan O', 'C dan N', 'Na dan Ci', 'K dan Mg'],
                'benar': 'H dan O'
            },
            {
                'soal': 'Apa simbol kimia untuk unsur hidrogen?',
                'pilihan': ['He', 'Hg', 'H', 'O'],
                'benar': 'H'
            },
            {
                'soal': 'Berapa sisi pada bangun ruang kubus?',
                'benar': '8'
            },
            {
                'soal': 'Berapakah nilai biner 1011 jika dikonversi ke desimal?',
                'benar': '11'
            }
        ]

        self.root = root
        self.root.title('Quiz')
        self.root.geometry(f"400x400+{int((self.root.winfo_screenwidth()/2) - (400/2))}+{int((self.root.winfo_screenheight()/2) - (400/2))}")


        self.soal = ttk.Label(self.root, text='')
        self.soal.pack()

        self.radioVar = ttk.StringVar(value=" ")

        self.all_radio = []
        for i in range(4):
            radio = ttk.Radiobutton(self.root, text="", value="", variable=self.radioVar, bootstyle="success")

            self.all_radio.append(radio)

        self.inputEntry = ttk.Entry(self.root)

        self.button = ttk.Button(text="Next", command=self.checkAnswer, bootstyle="outline-success")

        self.saatIni = 0
        self.benar = 0 

        random.shuffle(self.soalQuiz)
        self.loadQuestion()

        self.root.mainloop()

    def loadQuestion(self):
        self.soal.configure(text=self.soalQuiz[self.saatIni]['soal'])
        self.packUnpack()

    def packUnpack(self):
        if len(self.soalQuiz[self.saatIni]) > 2:
            for i, _ in enumerate(self.all_radio):
                self.all_radio[i].config(text=self.soalQuiz[self.saatIni]['pilihan'][i], value=self.soalQuiz[self.saatIni]['pilihan'][i])
                self.all_radio[i].pack(pady=7, padx=4)
            self.inputEntry.pack_forget()
            self.button.pack(pady=7)
        else:
            self.inputEntry.pack()
            for i, _ in enumerate(self.all_radio):
                self.all_radio[i].pack_forget()
            self.button.pack(pady=7)

    def checkAnswer(self):
        if len(self.soalQuiz[self.saatIni]) > 2:
            radioVar = self.radioVar.get()

            if radioVar != " ":
                if radioVar == self.soalQuiz[self.saatIni]['benar']:
                    self.benar += 1
                self.saatIni += 1

                self.checkRestQuestion()
            else:
                messagebox.showerror("HUFTT", "PILIH SALAH SATU OMAEE!")
        else:
            inputEntry = self.inputEntry.get()
            if inputEntry.strip() != "":
                if inputEntry == self.soalQuiz[self.saatIni]['benar']:
                    self.benar += 1
                self.saatIni += 1

                self.checkRestQuestion()
            else:
                messagebox.showerror("HUFTT", "ISI DULU OMAEE!")

    def checkRestQuestion(self):
        if self.saatIni < len(self.soalQuiz):
            if len(self.soalQuiz[self.saatIni]) > 2:
                self.radioVar.set(" ")
            else:
                self.inputEntry.delete(0, ttk.END)
            self.button.pack_forget()
            self.loadQuestion()
        else:
            self.showResult()
            

    def showResult(self):
        messagebox.showinfo("Hasil", f"Skor Akhir : {self.benar}/{len(self.soalQuiz)}")
        self.root.destroy()


if __name__ == '__main__':
    Quiz(ttk.Window())