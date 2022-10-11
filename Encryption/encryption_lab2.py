from tkinter import *
from random import randint
from tkinter import messagebox as mb
import random

global dic
dic = {}
def get_key(string):
    i = 0
    key = phrase_l = phrase_n = phrase_o = ""

    phrase_l = string.get().lower()
    phrase_o = phrase_l.split("_")
    phrase_n = string.get().split("_")

    for i in range(len(phrase_o)):
        if "key" in phrase_o[i]:
            key = phrase_n[i]
            break

    return key

def encrypt(phrase_key, step):

    encrypt_phrase = ""

    for i in phrase_key:
        encrypt_phrase += chr(ord(i) + step)
    return encrypt_phrase
def decipher(encrypt_phrase, step):
    #for without errors
    decipher_phrase = ""
    decipher_phrase += encrypt_phrase

    new_final_phrase = ""

    for i in decipher_phrase:
        new_final_phrase += chr(ord(i) - step)
    return new_final_phrase # return decipher phrase

def encrypt_btn():
    encrypt_phrase = ""
    phrase_key = pass_entry.get()

    key = get_key(pass_entry)

    step = randint(1, 10)
    dic.update({key: step})
    encrypt_phrase += encrypt(phrase_key, step)

    print(encrypt_phrase)

    answer = mb.askyesno("Зашифрованный текст",
                         f"Зашифрованный текст: \n{encrypt_phrase}\n" f"Сохранить результат в файл?")
    if answer:
        with open("Crypto.txt", "w", encoding="utf-8") as file:
            file.write(encrypt_phrase)


def decipher_btn():
    step = 0
    encryption_phrase = decipher_phrase = ""

    encryption_phrase = enc_pass_entry.get()

    key = get_key(key_entry)

    if key != get_key(pass_entry):
        step = randint(10, 20)
    else: step = dic[get_key(pass_entry)]

    decipher_phrase += decipher(encryption_phrase, step)

    answer = mb.askyesno("Расшифрованный текст",
                         f"Расшифрованный текст: \n{decipher_phrase}\n" f"Сохранить результат в файл?")
    if answer:
        with open("Crypto.txt", "w", encoding="utf-8") as file:
            file.write(decipher_phrase)

def clear():
    pass_entry.delete(0, END)
    enc_pass_entry.delete(0, END)
    key_entry.delete(0, END)

    dic.clear()

window = Tk()
window.geometry("350x350")
window.title("Crypto")

# -----------------------------pass-----------------------------#
pass_text = Label(window, text="Entry password:", width=15)
pass_text.place(x=0, y=5)

pass_entry = Entry(window, width=30)
pass_entry.place(height=30, x=0, y=30)

pass_encrypthon_btn = Button(window, width=10, justify="center", text="Encrypt", command=encrypt_btn)
pass_encrypthon_btn.place(height=25, x=200, y=30)
# -----------------------------pass_end-----------------------------#

# -----------------------------enc_pass-----------------------------#
enc_pass_text = Label(window, text="Entry encryption password:", width=20)
enc_pass_text.place(x=10, y=70)

enc_pass_entry = Entry(window, width=30)
enc_pass_entry.place(height=30, x=0, y=90)

deenc_pass_btn = Button(window, width=10, justify="center", text="Decipher", command=decipher_btn)
deenc_pass_btn.place(height=25, x=200, y=150)
# -----------------------------enc_pass_end-----------------------------#

# -----------------------------key-----------------------------#
key_text = Label(window, text="Entry key:", width=10)
key_text.place(x=0, y=130)

key_entry = Entry(window, width=30)
key_entry.place(height=30, x=0, y=150)
# -----------------------------key_end-----------------------------#

# -----------------------------clear_data-----------------------------#
clear_btn = Button(window, width=10, justify="center", text="Clear data", command=clear)
clear_btn.place(height=25, x=350 / 2 - 40, y=200)
# -----------------------------clear_data_end-----------------------------#

window.mainloop()