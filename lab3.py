from tkinter import StringVar, PhotoImage, Label, Tk, ttk
from random import randint, shuffle

params = {"title": "KeyGen228", "winsize": "400x400+1+10", "alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

root = Tk()
root.title(params['title'])
root.iconbitmap(default="icon.ico")
root.geometry(params['winsize'])
root.resizable(False, False)
root.attributes("-toolwindow", True)


KEYGEN = "XXXX-XXXX-XXXX-XXXX"
copy_btn_txt = "Copy"

KEY = StringVar(value=KEYGEN)
copytxt = StringVar(value=copy_btn_txt)

bg = PhotoImage(file='gb.png')
labelbg = Label(root, image=bg)
labelbg.place(x=-600, y=-50)

label = ttk.Label(text="Keygen by Google", font=("Arial", 14), background="#a6caf0", foreground="#F06767", padding=10)
label1 = ttk.Label(textvariable=KEY, font=("Arial", 13), background="#CCFF99", foreground="#3333FF", padding=8)

label.pack()
label1.pack(pady=30)


def generate(KEY, copytxt):
    SHUFFLED_KEYLIST = ''
    for forth_gen in range(4):
        KEYLIST = []
        for gen in range(3):
            a = randint(0, 25)
            KEYLIST += params['alphabet'][a]
        num = randint(0, 9)
        KEYLIST += str(num)
        shuffle(KEYLIST)
        SHUFFLED_KEY = ''.join(KEYLIST)
        SHUFFLED_KEYLIST += SHUFFLED_KEY
    KEYGEN = f'{SHUFFLED_KEYLIST[:4]}-{SHUFFLED_KEYLIST[4:8]}-{SHUFFLED_KEYLIST[8:12]}-{SHUFFLED_KEYLIST[12:16]}'
    KEY.set(value=KEYGEN)
    copytxt.set(value=copy_btn_txt)


def copytext(root):
    root.clipboard_clear()
    root.clipboard_append(label1['text'])
    copytxt.set(value='Copied!')


gen_btn = ttk.Button(text="Generate", padding=5, command=lambda: generate(KEY, copytxt))
copy_btn = ttk.Button(textvariable=copytxt, padding=5, command=lambda: copytext(root))

gen_btn.pack()
copy_btn.pack()

if __name__ == '__main__':
    root.mainloop()
