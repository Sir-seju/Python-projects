# This is a program that generates pi to the nth decimal place where n is an input provided by the user
import requests
import os
import time


def player_input():
    n = 0
    while n == 0:
        try:
            n = int(input('To how many decimal places do you want to find "Pi" in?: '))
        except:
            print("Wrong input! enter an integer!")
            continue
    return n


def pi_generator(n, x=0):
    # generate pi to 'n' decimal places
    print(f"Generating pi to {n} decimal places...")
    if n > 1000:
        a = 1000
        while n > 1000:
            r = requests.get(
                f"http://api.pi.delivery/v1/pi?start={x}&numberOfDigits={a}"
            )
            if not r.ok:
                print("Sorry! Server down! Please try again later")
            r_dict = r.json()
            pi = r_dict["content"]
            if x == 0:
                Pi = pi[:1] + "." + pi[1:]
                print(Pi, end="")
            else:
                print(pi, end="")
            n -= 1000
            x += 1000
        r = requests.get(f"http://api.pi.delivery/v1/pi?start={x}&numberOfDigits={n}")
        r_dict = r.json()
        pi = r_dict["content"]
        print(pi)
    else:
        r = requests.get(f"http://api.pi.delivery/v1/pi?start={x}&numberOfDigits={n}")
        if not r.ok:
            print("Sorry! Server down! Please try again later")
        r_dict = r.json()
        pi = r_dict["content"]
        Pi = pi[:1] + "." + pi[1:]
        print(Pi)


def play_again():
    while True:
        func = input('Play again? "y" / "n": ').upper()
        if func != "Y" and func != "N":
            print('Wrong input! choose "y" or "n"!')
            continue
        break
    return func == "Y"


# Pi Generator Program
os.system("cls")

print("Welcome to My Pi Generator Program!")
time.sleep(1)
while True:
    pi_generator(player_input())
    time.sleep(3)
    if play_again():
        continue
    else:
        break
print("Thanks for using Pi Generator Program")
print("-----------------")
time.sleep(2)
