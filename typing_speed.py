from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed(timest,timeend,userinp):
    time_delay = timeend - timest
    time_round = round(time_delay,2)
    speed = len(userinp)/time_round
    return round(speed)
               

while True:
    check = input("Should we run this? (yes/no) : ")
    if check == "yes":
        test = ["Lorem Ipsum is simply dummy text of the printing and typesetting industry.","It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.","Contrary to popular belief, Lorem Ipsum is not simply random text."]

        test1 = r.choice(test)
        print("     ********Typing Speed Calculator**********")
        print(test1)
        print()
        print()
        time1 = time()
        testinp = input("   Enter typing: ")
        time2 = time()

        print("Speed : ",speed(time1,time2,testinp), " w/sec ")
        print("Error : ",mistake(test1, testinp))
        
    elif check == "no":
        print("Thank you!!")
        break
    else:
        print("Enter valid input...")