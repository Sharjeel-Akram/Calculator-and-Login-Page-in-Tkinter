import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("Calculator")
root.geometry("335x352")

def Button_Click(item):
    global expression
    expression = expression + str(item)
    Input_Text.set(expression)

def Button_Clear(): 
    global expression 
    expression = "" 
    Input_Text.set("")

def Button_Equal():
    global expression
    result = str(eval(expression))
    Input_Text.set(result)
    expression = ""
 
expression = ""
 
Input_Text = StringVar()
 
Input_Frame = Frame(root, width=312, height=50, bd=0, highlightbackground="Blue", highlightthickness=5)
 
Input_Frame.pack(side=TOP)
 
Input_Field = Entry(Input_Frame, font=('Times New Roman', 18, 'bold'), textvariable=Input_Text, width=60, bg='Light Blue', bd=0, justify=RIGHT)
 
Input_Field.grid(row=0, column=0)
 
Input_Field.pack(ipady=10)
 
Buttons_Frame = Frame(root, width=312, height=270, bg="Blue")
 
Buttons_Frame.pack()
 
# first row
clear = Button(Buttons_Frame, text = "C", fg = "black",font=('Times New Roman', 10, 'bold'), width = 34, height = 3, bg = "Red", command = lambda: Button_Clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(Buttons_Frame, text = "/", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# second row
seven = Button(Buttons_Frame, text = "7", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(Buttons_Frame, text = "8", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(Buttons_Frame, text = "9", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(Buttons_Frame, text = "*", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
four = Button(Buttons_Frame, text = "4", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(Buttons_Frame, text = "5", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(Buttons_Frame, text = "6", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(Buttons_Frame, text = "-", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(Buttons_Frame, text = "1", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(Buttons_Frame, text = "2", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(Buttons_Frame, text = "3", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(Buttons_Frame, text = "+", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fifth row
 
zero = Button(Buttons_Frame, text = "0", fg = "black",font=('Times New Roman', 10, 'bold'), width = 22, height = 3, bg = "Light Blue", command = lambda: Button_Click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(Buttons_Frame, text = ".", fg = "black",font=('Times New Roman', 10, 'bold'), width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(Buttons_Frame, text = "=", fg = "black",font=('Times New Roman', 10, 'bold'),  width = 10, height = 3, bg = "Light Blue", command = lambda: Button_Equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


root.mainloop()