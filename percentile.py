from tkinter import *
import tkinter.messagebox

root = Tk()

#application main header

root.geometry("800x800")
root.title("Entrance Score Calculation")
label_main = Label(root, text = "Senior secondary board exam", fg = "white",relief = "ridge", bg = "black",font = ("Times New Roman", 32, "bold")).pack(fill = BOTH)

#an option to quit application

def quitting():
    exit()

b1= Button(root, text = "Exit application", width = "30", bg = 'red', fg = "white", font = ("Times New Roman", 16, "bold"), command = quitting)
b1.place(x = 600, y = 640)

#acessing file report card where values genertaed based on user input will be stored
file = open("report card.txt", 'w')

#getting user details (name)
fn = StringVar()
label_fname = Label(root, text = "First name:", fg = "white", relief = "ridge", bg = "grey", font = ("Times New Roman", 16, "bold")).place(x = 80, y = 120)
entry_fname = Entry(root, textvar = fn, width = "30", relief = "solid").place(x = 200, y = 120)

ln = StringVar()
label_lname = Label(root, text = "Last name:", fg = "white", relief = "ridge", bg = "grey", font = ("Times New Roman", 16, "bold")).place(x = 80, y = 200)
entry_lname = Entry(root, textvar = ln,width = "30", relief = "solid").place(x = 200, y = 200)

#initializing variables later required in the functions
total = 0
count = 0
count2 = IntVar()

#function to determine grade and grade point for each mark
def grade(m):
    global total
    global count
    m1 = int(m)
    if m1 in range(91, 101):
        file.write("A1 \t\t 10.0")
    elif m1 in range(81, 91):
        file.write("A2 \t\t 9.0")
    elif m1 in range(71, 81):
        file.write("B1 \t\t 8.0")
    elif m1 in range(61, 71):
        file.write("B2 \t\t 7.0")
    elif m1 in range(51, 61):
        file.write("C1 \t\t 6.0")
    elif m1 in range(41, 51):
        file.write("C2 \t\t 5.0")
    elif m1 in range(33, 41):
        file.write("D \t\t 4.0")
    elif m1 in range(21, 33):
        file.write("E1 \t\t 0.0")
    elif m1 in range(0, 21):
        file.write("E2 \t\t 0.0")
    total += m1
    count += 1
    count2.set(count)
    label_count = Label(root, text = f"Number of subjects done: ", fg = "black", font = ("Times New Roman", 16, "bold")).place(x = 80, y = 520)
    label_count2 = Label(root, textvar = count2,fg = "black", font = ("Times New Roman", 16, "bold")).place(x = 320, y = 520)
    file.write('\n\n')

#function to display the report card with all the user inputs
def display1():
    
    file.write("\t\t\t\t\t REPORT CARD\n\n")
    file.write("First Name: %s\n\nLast Name: %s" % (fn.get(), ln.get()))
    file.write('\n\n\n')
    file.write("------------------------------------------------------------------------------------------------------\n")
    file.write("Subject \t\t\t\t Marks \t\t Grade \t\t Grade Point\n\n")
    file.write("------------------------------------------------------------------------------------------------------\n")
    scores()

#function to get (user input) scores/marks

def scores():
    label_lname = Label(root, text = "Kindly choose the subject and fill in the grade. To enter next subject,click next. If done entering all subjects, click done.", fg = "black", bg = "yellow", font = ("Times New Roman", 16, "bold")).place(y = 320)
    global sub
    sub = StringVar()
    label_sub = Label(root, text = "Subject:", fg = "white", relief = "ridge", bg = "grey",font = ("Times New Roman", 16, "bold")).place(x = 80,y = 360)
    sub_cbse = ['Accountancy', 'Applied Mathematics','Biology' ,'Biotechnology', 'Business Studies', 'Chemistry', 'Computer Science', 'Economics', 'English - Core', 'English - Elective','Geography', 'History', 'Informatics Practices', 'Mathematics', 'Physics', 'Political Science', 'Psychology' ,'Sociology']
    sub.set("Select subject")
    droplist = OptionMenu(root, sub, *sub_cbse)
    droplist.config(width = 30)
    droplist.place(x = 200, y = 360)
    
    global mark
    mark = StringVar()
    label_mark = Label(root,text="Mark (out of 100): ", fg="white",relief="ridge", bg="grey",font=("Times New Roman",16,"bold")).place(x=80,y=440)
    entry_mark = Entry(root, textvar = mark, width = "30",relief="solid").place(x=290,y=440)        
        
    #function for user to indicate when done entering all marks
    
    def done():
        if mark.get() is not None:
            #check if entered mark is valid integer
            m=mark.get()
            if not m.isdigit():
                label_validity = Label(root, text = "INVALID MARK: Please enter only a positive integer!", fg = "black", bg = "red", font = ("Times New Roman", 12, "bold")).place(x=80,y = 480)
                scores()
            else:
                if len(sub.get()) > 15:
                    file.write("%s \t\t %s \t\t" % (sub.get(), mark.get()))
                elif len(sub.get()) == 7:
                    file.write("%s \t\t\t\t %s \t\t" % (sub.get(), mark.get()))
                else:
                    file.write(("%s \t\t\t %s \t\t" % (sub.get(), mark.get())))
                
                grade(m)
        percentage()

    #function to enter the next input marks
        
    def next1():
        #check if entered mark is valid integer
        m=mark.get()
        if not m.isdigit(): 
            label_validity = Label(root, text = "INVALID MARK: Please enter only a positive integer!", fg = "black", bg = "red", font = ("Times New Roman", 12, "bold")).place(x=80,y = 480)
            scores()
        else: 
            if len(sub.get())>15:
                file.write("%s \t\t %s \t\t" % (sub.get(), mark.get()))
            elif len(sub.get()) == 7:
                    file.write("%s \t\t\t\t %s \t\t" % (sub.get(), mark.get()))
            else:
                file.write("%s \t\t\t %s \t\t" % (sub.get(), mark.get()))
            grade(m)
            root.after(100,scores)

    n=Button(root, text="NEXT", width="30", bg="brown", fg="white",font=("Times New Roman",16,"bold"), command=next1)
    n.place(x=80,y=560)
    d=Button(root, text="DONE", width="30", bg='brown', fg="white",font=("Times New Roman",16,"bold"), command=done)
    d.place(x=490,y=560)

#function to calculate the percentage based on marks input    
def percentage():
    perc = round((total / count), 2)
    file.write("------------------------------------------------------------------------------------------------------\n\n")
    file.write(f"Aggregate Percentage is: {perc} %")
    tkinter.messagebox.showinfo("Calculation successful !!","Your report card is now ready. (Check file report card.txt)")  
    file.close()
    root.destroy()
b2 = Button(root, text = "Click here to enter scores", width = "30", bg = 'brown', fg = "white",font = ("Times New Roman", 16, "bold"), command = display1)
b2.place(x = 140, y = 280)

root.mainloop()
