from tkinter import *
from googletrans import Translator
import os
import csv

file_path = 'translate.csv'


def tran():
    text = t.get('1.0', END)
    a = translator.translate(text, dest='uz')
    t1.delete('1.0', END)
    t1.insert('1.0', a.text)


root = Tk()
root.geometry("600x600")
root.title('Translator')
root['bg'] = 'black'

translator = Translator()


def history():
    with open('translate.csv', "a", newline="\n") as f:

        header = ["Trans_word", "DOJ"]
        dict_writer = csv.DictWriter(f, header)
        if os.path.getsize('translate.csv') == 0:
            dict_writer.writeheader()


label = Label(root, fg='white', bg="black", text='Введите текст на английском')
label.place(relx=0.5, y=30, anchor=CENTER)

t = Text(root, width=35, height=5)
t.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='translate', command=tran)
btn.place(relx=0.5, y=180, anchor=CENTER)

t1 = Text(root, width=35, height=5)
t1.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()