from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! i clicked a Button")
    myLabel.pack()


myButton = Button(root, text="Click Here", command=myClick, fg="blue", bg="#ffffff")  # padx=50, pady=50)#state=DISABLED)
myButton.pack()

root.mainloop()
