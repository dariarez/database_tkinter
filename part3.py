import mysql.connector
import tkinter as tk

window = tk.Tk()

def dt():
    connection = mysql.connector.connect(host='localhost',
                                         database='datab',
                                         user='',
                                         password='')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM db")
    data = cursor.fetchall()
    text = tk.Text()
    text.pack()
    text.insert('1.0', data)
    cursor.close()
dt()

button = tk.Button(text='click', 
                    command=dt)
button.pack()


window.mainloop()