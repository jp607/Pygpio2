from tkinter import *


def count(v):
    for i in range(v):
        v -=1
        print(v)

window = Tk()

window.title('')

window.geometry('800x600')

label = Label(window)

b = Button(window, text ="5",command=lambda: count(5))

b.pack(side='left' )


b2 = Button(window, text ="10",command=lambda: count(10))

b2.pack(side='left')


b3 = Button(window, text ="15",command=lambda: count(15))

b3.pack(side='left')




window.mainloop()
