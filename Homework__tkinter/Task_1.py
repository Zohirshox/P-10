import tkinter as tk
from datetime import date

window = tk.Tk()
window.title("Birth year calculate")
window.geometry("350x250")
window.configure(bg='red')

def calculate():
    day = date.today()
    year = int(entry.get())
    if year <= 0 or year >= 2023:
        result_label["text"] = "Error....."
    else:
        age = day.year - year
        result_label["text"]=age


label_1 = tk.Label(text="Birth year:",bg='red')
label_1.place(x=20, y=10)

label_2 = tk.Label(text="Your age:", bg='red')
label_2.place(x=20, y=40)

result_label = tk.Label(text="0", bg='red')
result_label.place(x=80, y=40)

entry = tk.Entry(window)
entry.place(x=100, y=10)

button = tk.Button(window, text="Calculate", command=calculate)
button.place(x=90, y=75)

if __name__ == "__main__":
    window.mainloop()
