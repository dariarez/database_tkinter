import tkinter as tk
import mysql.connector

n = int(input('введіть число(від 1 до 13): '))

window = tk.Tk()

entry = tk.Entry()
entry.pack()
entry.insert(0, ('%s')%(n))
a = int(entry.get())

button = tk.Button(text='вивести')
button.pack()

def datab(a):
    if 13<a<1:
        print('вибачте, такого числа не існує в таблиці')
    else:
        connection = mysql.connector.connect(host='localhost',
                                         database='datab',
                                         user='',
                                         password='')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM db where id=('%s')"%(a))
        data = cursor.fetchall()
        label = tk.Label(text=data)
        label.pack()
        cursor.close()
datab(a)

window.mainloop()