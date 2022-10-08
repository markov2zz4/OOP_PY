from tkinter import *
from random import randint
from tkinter import messagebox as mb

def line_cr():
    line = ent_line.get() #Записываем в переменную line значение из Entry
    step = randint(1, 10) #Создаем шаг
    total_1 = {} #Словарь №1
    total_2 = {} #Словарь №2
    for i in line: #Считать из переменной line каждый символ
        new_i = ord(i) + step #шифруем символ(букву)
        total_1[chr(ord(i))] = ord(str(i)) #Добавить в словарь начальные символы
        total_2[chr(new_i)] = new_i  #Добавить в словарь зашифрованные символы
    answer = mb.askyesno("Info", f"{total_1}\n{total_2}") #Вывести в отдельное окно messagebox оба словаря
    if answer:#Если нажать "Да"
        my_file = open("Test_lab2.txt", "w+") #Открыть файл Test_lab2.txt
        my_file.write("Пример записи в файл") #Записать в файл
        my_file.close() #Закрыть файл

def encrypt():
    pass

def decipher():
    pass

def clear():
    pass_entry.delete(0, END)
    enc_pass_entry.delete(0, END)
    key_entry.delete(0, END)

window = Tk()
window.geometry("350x350")
window.title("Crypto")

#-----------------------------pass-----------------------------#
pass_text = Label(window,text="Entry password:", width=15)
pass_text.place(x=0,y=5)

pass_entry = Entry(window, width=30)
pass_entry.place(height=30, x=0, y=30)

pass_encrypthon_btn = Button(window, width=10, justify="center",text="Encrypt", command=encrypt)
pass_encrypthon_btn.place(height=25,x=200, y=30)
#-----------------------------pass_end-----------------------------#

#-----------------------------enc_pass-----------------------------#
enc_pass_text = Label(window,text="Entry encryption password:", width=20)
enc_pass_text.place(x=10,y=70)

enc_pass_entry = Entry(window, width=30)
enc_pass_entry.place(height=30, x=0, y=90)

deenc_pass_btn = Button(window, width=10, justify="center",text="Decipher", command=decipher)
deenc_pass_btn.place(height=25,x=200, y=150)
#-----------------------------enc_pass_end-----------------------------#

#-----------------------------key-----------------------------#
key_text = Label(window,text="Entry key:", width=10)
key_text.place(x=0,y=130)

key_entry = Entry(window, width=30)
key_entry.place(height=30, x=0, y=150)
#-----------------------------key_end-----------------------------#

#-----------------------------clear_data-----------------------------#
clear_btn = Button(window, width=10, justify="center",text="Clear data", command=clear)
clear_btn.place(height=25,x=350/2 - 40, y=200)
#-----------------------------clear_data_end-----------------------------#


window.mainloop()