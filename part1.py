import tkinter as tk
import mysql.connector

window = tk.Tk()

entry = tk.Entry()
entry.pack()
entry.insert(0, 'ffhfh')
a = entry.get()

entry = tk.Entry()
entry.pack()
entry.insert(0, 'fkfkfk')
b = entry.get()

entry = tk.Entry()
entry.pack()
entry.insert(0, 'rururu')
c = entry.get()

button = tk.Button(text='зберегти')
button.pack()

def datab(a, b, c):
    connection = mysql.connector.connect(host='localhost',
                                         database='db',
                                         user='',
                                         password='')
    cursor = connection.cursor()
    cursor.execute("insert into db (title) values ('%s')"%(a))
    cursor.execute("insert into db (title) values ('%s')"%(b))
    cursor.execute("insert into db (title) values ('%s')"%(c))
    connection.commit()
    cursor.close()

datab(a,b,c)

window.mainloop()