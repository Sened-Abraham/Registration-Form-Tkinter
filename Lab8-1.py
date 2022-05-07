
# Registration Form 



import tkinter.messagebox    
from tkinter import *

# assigning root variable to start tkinter
root= Tk()
root.geometry('500x500')
root.title('Registration Form')

# labeling the name and placing it according the given template
label= Label(root, text="Registration Form", width=20, font=('bold',20))
label.place(x=90,y=53)

# labeling the first requested entry
label1= Label(root, text="FullName", width=20, font=("bold",10))
label1.place(x=80,y=130)

# creating entry box for the first label
label1_entry1=Entry(root)
label1_entry1.place(x=240,y=130)


label2= Label(root, text="Email", width=20, font=("bold",10))
label2.place(x=68,y=180)

# creating entry box for the first label
label2_entry2=Entry(root)
label2_entry2.place(x=240,y=180)

# labeling the third element
label3= Label(root, text="Gender", width=20, font=("bold",10))
label3.place(x=70,y=230)
# given a var for both radio button , to indicate one is selected at a time
var=IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female", padx=5, variable=var, value=2).place(x=290,y=230)

# labeling the fourth element
label4= Label(root, text="country", width=20, font=("bold",10))
label4.place(x=70,y=280)

# creating the lists of countries
list=['Eritrea','UAE','Ethiopia','Sudan','UK','USA','Singapore','South Africa']
# craeting dropdown list with variable assigned to value
value=StringVar()
dropdownlist=OptionMenu(root,value, *list)
dropdownlist.config(width=15)
value.set('Select your country')
dropdownlist.place(x=240,y=280)

# labeling the fifth element
label5= Label(root, text="Programming", width=20, font=("bold",10))
label5.place(x=85,y=330)



var1=IntVar()
Checkbutton(root,text='java',variable=var1).place(x=235,y=330)

var2=IntVar()
Checkbutton(root,text="python",variable=var2).place(x=290,y=330)


def save_info():
    if label1_entry1.get() != '' and label2_entry2.get() !='': 
        handle=open("information.txt","w")   
        handle.write(label1_entry1.get())
        handle.write("\n")
        handle.write(label2_entry2.get())
        handle.write("\n")
        if var.get() !=0:    
            if var.get()==1:
                handle.write("Male")
                handle.write("\n")
            else:
                handle.write("Female")
                handle.write("\n")
            if value.get() != '':    
                handle.write(str(value.get()))  
                handle.write("\n")
                if var1.get() and var2.get() !=0:  
                    handle.write("Java Python")
                elif var1.get()!=0:   
                    handle.write("Java")
                elif var2.get()!=0:    
                    handle.write("Python")
                    handle.close()
                else:
                    tkinter.messagebox.showwarning("Empty Fields", "You must enter all the needed information")  # throwing error message in case the user skips any entry
            else:
                tkinter.messagebox.showwarning("Empty Fields", "You must enter all the needed information")
        else:
            tkinter.messagebox.showwarning("Empty Fields", "You must enter all the needed information")
    else:
        tkinter.messagebox.showwarning("Empty Fields", "You must enter all the needed information")


Button(root, text="Submit", width=20, bg='brown',fg='white',command=save_info).place(x=180,y=380)

root.mainloop()     # to stop the loop of the tkinter
