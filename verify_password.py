#lets create a password verifier 
import time

password = ""

#Enter a password with mre than 
def enter_password():
    global password 
    while True:
        password = input('Enter a password in the range of 8-14 characters that contains letters, numbers and a symbol')
        if 7 < len(password):
            pass
        else:
            print('entered password too short, kindly re-enter a password in the range of 8-14 characters')
            continue 
        if len(password) <15:
            return password
        else:
            print('entered password too long, kindly re-enter a password in the range of 8-14 characters')
            continue 

def check_password(text):
    alphabets = 0
    numerics = 0
    special = 0
    s_c = '~`!@#$%^&*()-_+={}[]|\/:;"\'<>,.?'
    
    for char in text:
        if char.isalpha():
            alphabets+=1
        elif char.isdigit():
            numerics+=1
        elif char in s_c:
                    special+=1
        else:
            print('Bad password')
            return False
    if alphabets > 0  and numerics > 0 and special > 0:
        return True
    else:
        return False
       

print('-'*50)
time.sleep(.5)
print('Welcome to this Pasword Verfication program')
time.sleep(.5)
A = 0
while A == 0:
    B = check_password(enter_password())
    if B:
        print(f'Password Creation success! Your pasword is {password}')
        A+=10
    else:
        print('Wrong password input! Please follow instructions and try again')
        time.sleep(.5)
        continue