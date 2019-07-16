from tkinter import *

root = Tk()

v = StringVar()                    #should declare v as StringVar() so that we can change it's value

def printField(event):
   #entry_1.delete(0, END)   -> can be used to delete the previously displaying value in the entry field
   s = entry_1.get()               #get() is used to retrieve the text entered in the entry field
   print(s)
   v.set(s)                        #set() is used to set the value of the variable v so that it is updated in the label


label_1 = Label(root, text="Image URL")
label_2 = Label(root, textvariable=v)
entry_1 = Entry(root)
entry_1.insert(0, "Enter URL")
button_1 = Button(root, text="Submit", fg="red")
button_1.bind("<Button-1>", printField)

label_1.grid(row=0, sticky=E)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, columnspan=2)
label_2.grid(row=2, columnspan=2)




root.mainloop()

#References
# https://effbot.org/tkinterbook/entry.htm
# https://stackoverflow.com/questions/17125842/changing-the-text-on-a-label
# http://effbot.org/tkinterbook/label.htm



