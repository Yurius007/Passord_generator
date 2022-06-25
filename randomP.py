import random as r
from tkinter import *
import webbrowser as web

mw = Tk()
mw.geometry("300x280")
mw.title('Генератор паролів')

global length
lenght = 8
global turn
turn = IntVar()

abcsl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abcsu = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
syms = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
lists = [abcsl, abcsu, nums]

def generator():    # функція що генерує паролі
    
    i = 1
    pw = ''
    pwsg = ''

    while i <= lenght:

        pwsg = lists[r.randint(0, len(lists) - 1)]

        pw = pw + pwsg[r.randint(0, len(pwsg) - 1)]
        i = i + 1    

    pw_list.insert(0,pw)

def syms_enabler():     # функція вмикач додаткових символів

    global lists

    if(turn.get()==1):
        lists = [abcsl, abcsu, nums, syms]
        print("syms enabled")
    else:
        lists = [abcsl, abcsu, nums]
        print("syms disabled")
    
def submit():       # функція підтвердження змін в полі вводу len_input
    global lenght
    lenght = int(len_input.get())

def pw_list_cleaner():      # функція очистки списку pw_list
    pw_list.delete(0, END)

def pw_check_open():        # функція перевірки паролю
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    url = 'https://password.kaspersky.com/'
    web.get(chrome_path).open(url)

len_alert = Label(mw, text = "Довжина пароля:") # змінна напису Довжина пароля
len_alert.place(x=10,y=30)

len_input = Entry(mw) # змінна поля вводу
len_input.insert(0,str(lenght))
len_input.place(x=10,y=50)

submit_btn = Button(mw, text = "Підтвердити", command=submit) # змінна кнопки Підтвердити 
submit_btn.place(x=10,y=95)

add_syms = Checkbutton(mw, text = "Додаткові символи", variable=turn, command=syms_enabler) # змінна галочки Додаткові символи
add_syms.place(x=10,y=70)

generate_btn = Button(mw, text = "Генерувати", height = 2, width = 18, command=generator) # змінна кнопки Генерувати
generate_btn.place(x=10,y=130)

pw_list = Listbox(mw) # змінна списку паролів
pw_list.place(x=165,y=30)

pw_list_clear = Button(mw, text = "Очистити", command=pw_list_cleaner) # змінна кнопки очищення
pw_list_clear.place(x=170,y=235)

pw_check = Button(mw, text = "Перевірити пароль", command=pw_check_open) # змінна кнопки Перевірити пароль
pw_check.place(x=170,y=205)

mw.mainloop()