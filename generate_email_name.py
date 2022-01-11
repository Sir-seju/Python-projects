def play_input():
    while True:
        n = input( 'Enter here: ').lower().split()
        try:
            firstname, lastname = n[0], n[1]
        except ValueError:
            print ('wrong imput, enter your fullname correctly')
            continue
        if firstname.isalpha() and lastname.isalpha():
            return firstname, lastname
        else:
            print ('wrong imput, enter your fullname correctly')
            continue

def email(f,l):
    """This is a function that creates emails for people"""
    email = f[0:1] + l + '@gmail.com'
    print (f' your email is : {email}')
    
import time
print("""Welcome to the emailer app, enter your full name in [firstname lastname]\
 format so i can generate an email for you""")

time.sleep(1.5)    
email(*play_input()) 
