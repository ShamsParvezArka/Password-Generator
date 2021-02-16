import random
import string
import pyperclip

def core():
    x0 = string.ascii_letters # type A-Z,a-z
    x1 = string.digits        # type 0-1
    x2 = string.punctuation   # type !@#$%^&*()_+=-~`[]{}';<>/?\
    
    length = input(">>> Input Password length:")
    usr_input = input(">>> Input Password strenght [0] low [1] medium [2]high :")
    
    gen_lst = []              # Initialize password in a list

    for i in range(int(length)):
        if usr_input == '0':
            tmp_lst = random.choice(x0)
        elif usr_input == '1':
            tmp_lst = random.choice(x0 + x1)
        elif usr_input == '2':
            tmp_lst = random.choice(x0 + x1+ x2)
        gen_lst.append(tmp_lst)
        
        
    output = ''.join(gen_lst) # Compile the list in to a word
    print(output, end="      ")
    print("[password copied in the clipboard!]")
    pyperclip.copy(output)    # Copy generated password
    input(">>> Press any key to exit")
    
core()
