import tkinter as tk
from tkinter import ttk,messagebox
def display():

    try:

        # Check subject names are filled
        if (name1.get().strip() == "" or
            s1.get().strip() == "" or
            s2.get().strip() == "" or
            s3.get().strip() == "" or
            s4.get().strip() == "" or
            s5.get().strip() == ""):

            messagebox.showerror(
                "Input Error",
                "Please fill all subject names or student name."
            )
            return

        # Check subject names contain only letters
        subjects = [
            name1.get(),
            s1.get(),
            s2.get(),
            s3.get(),
            s4.get(),
            s5.get()
        ]

        for subject in subjects:

            subject = subject.replace(" ", "")

            if not subject.isalpha():
                messagebox.showerror(
                    "Input Error",
                    "Subject names or student name must contain only alphabets."
                )
                return

        # Get marks
        x1 = sm1.get()
        x2 = sm2.get()
        x3 = sm3.get()
        x4 = sm4.get()
        x5 = sm5.get()

        marks = [x1, x2, x3, x4, x5]

        # Check marks range
        for mark in marks:

            if mark < 0 or mark > 100:
                messagebox.showerror(
                    "Input Error",
                    "Marks must be between 0 and 100."
                )
                return

        # Total
        y = x1 + x2 + x3 + x4 + x5
        total1.set(y)

        # Percentage
        z = (y / 500) * 100
        percentage1.set(round(z, 2))

        # Grade
        if z >= 90:
            grade1.set("A+")

        elif z >= 80:
            grade1.set("A")

        elif z >= 70:
            grade1.set("B")

        elif z >= 60:
            grade1.set("C")

        elif z >= 50:
            grade1.set("D")

        else:
            grade1.set("F")

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{e}"
        )

    output1 = ttk.Label(window,textvariable=total1,font=("Calibri",24,"bold"),background="green")
    output1.grid(column=2,row=8,columnspan=4,stick="ewns")

    output2 = ttk.Label(window,textvariable=percentage1,font=("Calibri",24,"bold"),background="green")
    output2.grid(column=2,row=9,columnspan=4,stick="ewns")
    
    output3 = ttk.Label(window,textvariable=grade1,font=("Calibri",24,"bold"),background="green")
    output3.grid(column=2,row=10,columnspan=4,stick="ewns")

def clear1():
    sm1.set(value=" ")
    sm2.set(value=" ")
    sm3.set(value=" ")
    sm4.set(value=" ")
    sm5.set(value=" ")
    total1.set(value=" ")
    percentage1.set(value=" ")
    grade1.set(value=" ")
    s1.set(value=" ")
    s2.set(value=" ")
    s3.set(value=" ")
    s4.set(value=" ")
    s5.set(value=" ")



window = tk.Tk()
window.title(" Subject Percentage Calculator")
window.geometry("800x400")

for i in range(4):
    window.columnconfigure(i,weight=1)

for i in range(12):
    window.rowconfigure(i,weight=1)


heading = ttk.Label(window,
                    text="Student Subject Marks Calculator",
                    font=("Calibri",24,"bold"),
                    foreground="black",
                    background="light green")

heading.grid(column=0,row=0,columnspan=4,stick="ewns")

name = ttk.Label(window,
                    text="Student name : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="pink")

name.grid(column=0,row=1,columnspan=2,stick="ewns")
name1 = tk.StringVar()
Inputname = ttk.Entry(window,
                    font=("Calibri",24,"bold"),
                    textvariable=name1)

Inputname.grid(column=2,row=1,columnspan=4,stick="ewns")


subject1 = ttk.Label(window,
                    text="Subject 1 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")
subject2 = ttk.Label(window,
                    text="Subject 2 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")
subject3 = ttk.Label(window,
                    text="Subject 3 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")
subject4 = ttk.Label(window,
                    text="Subject 4 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")
subject5 = ttk.Label(window,
                    text="Subject 5 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")

subject1.grid(column=0,row=2,stick="ewns")
subject2.grid(column=0,row=3,stick="ewns")
subject3.grid(column=0,row=4,stick="ewns")
subject4.grid(column=0,row=5,stick="ewns")
subject5.grid(column=0,row=6,stick="ewns")

s1 = tk.StringVar()
s2 = tk.StringVar()
s3 = tk.StringVar()
s4 = tk.StringVar()
s5 = tk.StringVar()

Inputsubject1 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                    textvariable=s1)
Inputsubject2 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                     textvariable=s2)
Inputsubject3 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                     textvariable=s3)
Inputsubject4 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                     textvariable=s4)
Inputsubject5 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                     textvariable=s5)

Inputsubject1.grid(column=1,row=2,stick="ewns")
Inputsubject2.grid(column=1,row=3,stick="ewns")
Inputsubject3.grid(column=1,row=4,stick="ewns")
Inputsubject4.grid(column=1,row=5,stick="ewns")
Inputsubject5.grid(column=1,row=6,stick="ewns")

Marksubject1 = ttk.Label(window,
                    text="Subject Marks 1 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue",
                   )
Marksubject2 = ttk.Label(window,
                    text="Subject Marks 2 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")
Marksubject3 = ttk.Label(window,
                    text="Subject Marks 3 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")
Marksubject4 = ttk.Label(window,
                    text="Subject Marks 4 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")
Marksubject5 = ttk.Label(window,
                    text="Subject Marks 5 : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="blue")

Marksubject1.grid(column=2,row=2,stick="ewns")
Marksubject2.grid(column=2,row=3,stick="ewns")
Marksubject3.grid(column=2,row=4,stick="ewns")
Marksubject4.grid(column=2,row=5,stick="ewns")
Marksubject5.grid(column=2,row=6,stick="ewns")

sm1 = tk.IntVar(value=" ")
sm2 = tk.IntVar(value=" ")
sm3 = tk.IntVar(value=" ")
sm4 = tk.IntVar(value=" ")
sm5 = tk.IntVar(value=" ")
total1 = tk.IntVar()
percentage1 = tk.DoubleVar()
grade1 = tk.StringVar()



InputMarksubject1 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                    textvariable=sm1)
InputMarksubject2 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                    textvariable=sm2)
InputMarksubject3 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                    textvariable=sm3)
InputMarksubject4 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                    textvariable=sm4)
InputMarksubject5 = ttk.Entry(window,
                    font=("Calibri",24),
                    foreground="black",
                    background="blue",
                    textvariable=sm5)

InputMarksubject1.grid(column=3,row=2,stick="ewns")
InputMarksubject2.grid(column=3,row=3,stick="ewns")
InputMarksubject3.grid(column=3,row=4,stick="ewns")
InputMarksubject4.grid(column=3,row=5,stick="ewns")
InputMarksubject5.grid(column=3,row=6,stick="ewns")

button = tk.Button(window,text=" Sumbit ",font=("Calibri",24),
                    foreground="black",
                    background="grey",
                    command=display)
button.grid(column=0,row=7,columnspan=4,stick="ewns")



total = ttk.Label(window,
                    text="Total Marks : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="dark green",
                    )
percentage = ttk.Label(window,
                    text=" Percentage : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="dark green")
grade = ttk.Label(window,
                    text=" Grade : ",
                    font=("Calibri",24,"bold"),
                    foreground="white",
                    background="dark green")


total.grid(column=0,row=8,columnspan=2,stick="ewns")
percentage.grid(column=0,row=9,columnspan=2,stick="ewns")
grade.grid(column=0,row=10,columnspan=2,stick="ewns")

button1 = tk.Button(window,text="clear",foreground="black",
                    background="red",command=clear1)
button1.grid(column=0,row=11,columnspan=4,stick="ewns")


window.mainloop()