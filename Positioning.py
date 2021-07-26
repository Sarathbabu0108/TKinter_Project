from tkinter import *

root = Tk()
# creatin a label widget
myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
myLabel2 = Label(root, text="My Name Is Sarath Babu").grid(row=1, column=2 )
# showing it on to the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=2 )

root.mainloop()