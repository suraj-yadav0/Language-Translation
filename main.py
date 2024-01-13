from tkinter import*
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root['bg'] = 'skyblue'

root.title('Language Translator')
Label(root, text="Language Translator", font="Arial 20 bold").pack()

Label(root, text="Enter Text", font='arial 13 bold' , bg='white smoke').place(x=165,y=90)

Input_text = Entry(root, width=60)
Input_text.place(x=30,y=130)
Input_text.get()

root.mainloop()