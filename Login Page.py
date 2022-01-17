import tkinter
from tkinter import *
root = tkinter.Tk()
root.geometry('400x250')
root.configure(bg = 'Light Blue')
def Create_first_GUI():
    Username = Label(root, text = 'Username: ', bg = 'Red').place(x=30,y=40)
    Passwrord = Label(root, text = 'Password:  ', bg = 'Red').place(x=30,y=65)
    
    User_TextField = Entry(root, width = 30, bg = 'White')
    User_TextField1 = User_TextField.place(x=100,y=40)
    
    Pass_TextField = Entry(root, width = 30, bg = 'White')
    Pass_TextField1 = Pass_TextField.place(x=100,y=65)
    
    Hint = Label(root, text = 'Hint: N......3',bg = 'Green').place(x=120,y=160)
    
    Submit = Button(root, text = 'Submit', bg = 'Red', command = lambda: ButtonPressed(User_TextField,Pass_TextField)).place(x=30,y=90)
    
    root.mainloop()
    
def ButtonPressed(Username,Password):
    Username_value = Username.get()
    Password_value = Password.get()
    print('Button Pressed')
    print(Username_value)
    print(Password_value)
    if Username_value == "Namal" and Password_value == "123":
        root.destroy()
        root1 = tkinter.Tk()
        root1.geometry('400x250')
        root1.configure(bg = 'Light Blue')
        Text = Label(root1, text = 'Hey Handsome! Welcome to Namal Institute Mianwali',bg = 'Red').place(x=50,y=50)
        root1.mainloop()
    else:
        Invalid = Label(root, text = 'Invalid Username or Password! Please Try AGain').place(x=50,y=130)
    
Create_first_GUI()