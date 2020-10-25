from tkinter import*

def callback():
    print("cool....")
root = Tk()
root.geometry('450x350')
root.title("DL Test Appointment Form")

label_0 = Label(root, text="Input Application Details",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Application Number",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="DOB (DD/MM/YYYY)",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

# label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
# label_3.place(x=70,y=230)
# var = IntVar()
# Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
# Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Captcha",width=20,font=("bold", 10))
label_4.place(x=70,y=230)


entry_4 = Entry(root)
entry_4.place(x=240,y=230)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=callback()).place(x=180,y=280)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")