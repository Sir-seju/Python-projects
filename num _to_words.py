#This is a program that outputs numbers to words. 
import os
import time

def player_input():
    #Take and verify input
    global num
    while True:
        num= input('Enter an integer: ')
        if num.isdigit():
            num=int(num)
            if num <1000000000:
                return num
            else:
                print ('Enter an integer less than 1000000000')
                continue
        else:
            print('Wrong input!')
            continue

def process_num(num):
    global num_list
    num_list = [0,0,0,0,0,0,0,0,0]
    num_list[0] = num//100000000%10 #Hundred Millions place
    num_list[1] = num//10000000%10 	#Ten Millions place
    num_list[2] = num//1000000%10 	#Millions place
    num_list[3] = num//100000%10 	#Hundred-thousands place
    num_list[4] = num//10000%10 	#Ten-thousands place
    num_list[5] = num//1000%10 		#Thousands place
    num_list[6] = num//100%10 		#Hundreds place
    num_list[7] = num//10%10 		#Tens place
    num_list[8] = num//1%10 		#Ones place
    return

dict_units={str(x):y for x,y in zip(range(10),['','one','two','three','four','five','six','seven','eight','nine'])}
dict_teens={str(x):y for x,y in zip(range(11,20),['eleven', 'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'])}
dict_tens={str(x):y for x,y in zip(range(10,91,10),['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty','seventy','eighty','ninety'])}
dict_hundreds={str(x):y for x,y in zip(range(100,901,100),['one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred'])}

def idenum(num):
    answer= ""
    if num == 0:
        answer= 'zero'
        return answer
    if 1 <= num < 10:
        answer = dict_units[str(num)]
        return answer
    elif num in range(10,91,10):
        answer = dict_tens[str(num)]
        return answer
    elif 10 < num < 20:
        answer = dict_teens[str(num)]
        return answer
    elif 20 < num < 100: 
        answer = dict_tens[(str(num)[0] + '0')] +' '+ dict_units[(str(num)[1])]
        return answer
    elif num in range(100,901,100):
        answer = dict_hundreds[str(num)]
        return answer
    elif 100< num < 1000:
        num = str(num)
        if num[1] == 0:
            answer = dict_hundreds[num[0] + '00']+' and  '+dict_units[num[2]]
            return answer
        elif num[1] == 1:
            answer = dict_hundreds[num[0] + '00']+' and  '+dict_teens[num[1]+num[2]]
            return answer
        else:
            answer = dict_hundreds[num[0] + '00']+' and '+dict_tens[num[1] + '0'] +' '+dict_units[num[2]]
            return answer
    elif 1000<= num <1000000:
        answer+= idenum(num_list[3]*100 + num_list[4]*10 +num_list[5]) + ' thousand '
        if not num_list[6]==num_list[7]==num_list[8]==0:
            answer+= idenum(num_list[6]*100 + num_list[7]*10 +num_list[8])
        return answer
    elif 1000000 < num < 1000000000:
        answer+= idenum(num_list[0]*100 + num_list[1]*10 + num_list[2]) + ' million '
        if not num_list[3]==num_list[4]==num_list[5]==0:
            answer+= idenum(num_list[3]*100 + num_list[4]*10 + num_list[5]) + ' thousand '
            if not num_list[6]==num_list[7]==num_list[8]==0:
                answer+= idenum(num_list[6]*100 + num_list[7]*10 + num_list[8])
        return answer

def display_answer(answer):
    x = time.time()
    print(answer)
    print(f'Executed in {time.time()-x} seconds')


def play_again():
    while True:
        func = input('Play again? "y" / "n": ').upper()
        if func!= 'Y' and func != 'N':
            print('Wrong input! choose "y" or "n"!')
            continue
        break
    return func== 'Y'


#Num Converter Program
os.system('cls')

print('Welcome to Num Converter Program!')
time.sleep(1)
while True:
    process_num(player_input())
    display_answer(idenum(num))
    if play_again():
        continue
    else:
        break
print ("Thanks for using Num Converter Program")
print("-----------------")
time.sleep(2)
    