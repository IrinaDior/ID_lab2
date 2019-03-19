from random import randint
import datetime
"""it is the subscriber account system """
MTS={}
list_number=["0956500044","095226288","0952425399","0956435699","0666419388"]
def create_account (dict_abonents, phonenumber,name,surname,amountofmoney=0):
    """create account for new abonent"""
    #print("function is create_account")
    #print(phonenumber,name,surname)
    dict_abonents[phonenumber] = {
            "name" :name,
            "surname" :surname,
            "balance": 0
        }



def print_info(dict_abonents, phone_number):
    print("Name: " + str(dict_abonents[phone_number]["name"]))
    print("Surname: " + str(dict_abonents[phone_number]["surname"]))
    print("Balance: " + str(dict_abonents[phone_number]["balance"]))

    if "reccall" in dict_abonents[phone_number]:
        print("Last incoming call: " + str(dict_abonents[phone_number]["reccall"]) + " at " + str(dict_abonents[phone_number]["lastrecdata"]))
    else:
        print("no calls avaliable")
    if "lastcall" in dict_abonents[phone_number]:
        print("Last outcoming  call: " + str(dict_abonents[phone_number]["lastcall"]) + " at " + str(dict_abonents[phone_number]["lastcalldata"]))
    else:
        print("no calls avaliable")


def call(phone_number):
    pass

def print_phone_numbers(list_phones):
        i=0
        for number in list_phones:
            i+=1
            print("{} - +38{}".format(i,number))

def make_call(dict_abonents, phonen):
        number = "0" + str(randint(630000000, 990000000))
        dict_abonents[phonen]["lastcall"] = number
        dict_abonents[phonen]["lastcalldata"] = datetime.datetime.now()
        dict_abonents[phonen]["balance"] = int(dict_abonents[phonen]["balance"]) - 2
        print(phonen + " makes call to " + number)

def put_money_score (dict_abonents, phonen):
    print("How much money do you want to put?")
    num = input()
    dict_abonents[phonen]["balance"] = num
    print("Balance is updated")

def rec_call(dict_abonents, phonen):

    number = "0" + str(randint(630000000, 990000000))
    dict_abonents[phonen]["reccall"] = number
    dict_abonents[phonen]["lastrecdata"] = datetime.datetime.now()
    dict_abonents[phonen]["balance"] = int(dict_abonents[phonen]["balance"]) - 1
    print(phonen + " gets call from " + number)


if __name__ == "__main__":
    print("please choose phone number")
    print_phone_numbers(list_number)
    
    i_number = int(input())

    if i_number > 0 and i_number <=len(list_number):
        print ("OK!,thanks for our answer,please enter your name")
        name = input("please enter your name: ")
        surname = input("please enter your surname: ")
        create_account(MTS, list_number[i_number-1],name,surname)
        print_info(MTS,list_number[i_number-1])
        print("You can't perform calls with an empty account! Let's update your balance: ")
        put_money_score(MTS, list_number[i_number - 1])
        print_info(MTS, list_number[i_number - 1])
        print("System will perform calls to activate account")
        make_call(MTS, list_number[i_number - 1])
        rec_call(MTS, list_number[i_number - 1])
        print("Last stats: ")
        print_info(MTS, list_number[i_number - 1])
    else:
        print("sorry,number is not correct")
    


