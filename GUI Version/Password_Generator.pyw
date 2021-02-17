import random
import string
import pyperclip
from tkinter import *



def core():
    entry0.delete(0, 'end')

    x0 = string.ascii_letters # type A-Z,a-z
    x1 = string.digits        # type 0-1
    x2 = string.punctuation   # type !@#$%^&*()_+=-~`[]{}';<>/?\
    
    length = entry1.get()
    pass_strength = var.get()
    
    gen_lst = []              # Initialize password in a list

    for i in range(int(length)):
        if pass_strength == 1:
            tmp_lst = random.choice(x0)
        elif pass_strength == 2:
            tmp_lst = random.choice(x0 + x1)
        elif pass_strength == 3:
            tmp_lst = random.choice(x0 + x1+ x2)
        gen_lst.append(tmp_lst)
        
        
    output = ''.join(gen_lst) # Compile the list in to a word
    entry0.insert(10, output)

def copy():
    output = entry0.get()
    pyperclip.copy(output)


window = Tk()
var = IntVar()


window.title('Password Generator')                  # Programme Title
window.geometry('410x90')  

lbl0 = Label(window, text = 'Generated Password') 
lbl0.grid(row = 0, column = 0)

entry0 = Entry(window, width = 36)                  # Output
entry0.grid(row = 0, column = 1, sticky = 'w')

dwn_btn0 = PhotoImage(file = 'icons/button0.png')

btn0 = Button(window, image = dwn_btn0, borderwidth = 0, command = copy)     # Copy Generated password
btn0.grid(row = 0, column = 2)

lbl1 = Label(window, text = ' Password Length')               # Input: pass length
lbl1.grid(row = 1, column = 0)

entry1 = Entry(window, width = 5)
entry1.grid(row = 1, column = 1, sticky = 'w')

lbl2 = Label(window, text = 'Password Strength')             # Input: pass strength
lbl2.grid(row = 2, column = 0, sticky = 'e')

r_button0 = Radiobutton(window, text = 'LOW', variable = var, value = 1)
r_button0.grid(row = 2, column = 1, sticky = 'w')

r_button1 = Radiobutton(window, text = 'MEDIUM', variable = var, value = 2)
r_button1.grid(row = 2, column = 1)

r_button2 = Radiobutton(window, text = 'STRONG', variable = var, value = 3)
r_button2.grid(row = 2, column = 1, sticky = 'e')


dwn_btn1 = PhotoImage(file = 'icons/button1.png')

btn1 = Button(window, image = dwn_btn1, borderwidth = 0, command = core)         # Password generating key
btn1.grid(row = 2, column = 2)

royality = Label(window, text = 'Author :: Shams Parvez Arka' )
royality.grid(row = 3, column = 1) 


window.mainloop()







