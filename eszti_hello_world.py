# Lukács Eszti's Hello World program! =)

import sys 

def welcome_user():
    try:
        if len(str(sys.argv[1])) < 1:
            sys.argv[1] = World
        print("Hello ", " ".join(sys.argv[1:]), "!", sep='')
    except:
        print("Wello World!")

welcome_user()




