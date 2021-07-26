from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name", command=myClick, fg="blue",
                  bg="#ffffff")  # padx=50, pady=50)#state=DISABLED)
myButton.pack()

root.mainloop()
