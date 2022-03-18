import webbrowser
from tkinter import *

root = Tk()

root.title('Open web browser')
root.geometry('300x200')


def google():
    webbrowser.open('google.com')


Button(root, text='Open Google', command=google).pack(pady=20)
root.mainloop()
