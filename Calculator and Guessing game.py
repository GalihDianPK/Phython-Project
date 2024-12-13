for i in range(5) :
    print("-", end="")
    
print('Welcome to my Project', end="")

for i in range(5) :
    print("-", end="")
print("-")
print("")

games = ["kalkulator sederhana", "game tebak angka"]

def game():
    for i in range(4) :
        print("-", end="")

    print("Please choose the game", end="")

    for i in range (4) :
        print("-", end="")
    print("")

    print("1. " + games[0])
    print("2. " + games[1])
    print("3. " + games[2])
    print("")

def pembuka() :
    for i in range(9) :
        print("-", end="")
    print("Welcome boy!", end="")
    for i in range(9) :
        print("-", end="")
    print("")
    
correctPassword = "galih002"
attempts = 3
falseAttempts = 0 
waitTime = 5
isLoggedIn = False
import time

while not isLoggedIn :
    while falseAttempts != attempts :
        password = (input("Input password : "))
        print("")
        if password == correctPassword :
            pembuka()
            game()
            isLoggedIn = True
            break
        else : 
            falseAttempts += 1
            print(f"Password wrong!, you have {attempts-falseAttempts} attempts remaining")
        if falseAttempts == attempts : 
            print("Wait a seconds before you try again")
            time.sleep(waitTime)
            print("you can try again now!")
            falseAttempts = 0
            break

    choose = int(input("masukkan angka (1-3) : "))
    print ("")

def kalkulatorSederhana() :
    angkaInput = float(input("masukkan angka : "))
    angkaInput2 = float(input("masukkan angka : "))
    operasiJumlah = input("masukkan inputan (+,-,*,/): ")

    if operasiJumlah == "+" :
        result = angkaInput + angkaInput2 
        print(f"the result is : {result}")
    elif operasiJumlah == "-" :
        result = angkaInput - angkaInput2
        print(f"the result is : {result}")
    elif operasiJumlah :
        result = angkaInput * angkaInput2
        print(f"the result is : {result}")
    elif operasiJumlah :
        result = angkaInput / angkaInput2 
        print(f"the result is : {result}")

def lastChoice() :
    tryAgain1 = input("apakah kamu ingin bermain lagi? (y/n) : ")
    if tryAgain1 == "y" :
            kalkulatorSederhana()
            lastChoice()
    else :
            print("")
            for i in range(15) :
                print("-", end="")
            print("Game end", end="")
            for i in range(15) :
                print("-", end="")
            print("")
            for i in range(5) :
                print("-", end="")
            print("thank you for your support!", end="")
            for i in range(5) :
                print("-", end="")
            print("")

def tebakAngka() :
    import random
    print("aku adalah angka di kisaran 1-15 ! ")
    angkaAcak = random.randrange(1, 15)
    tebakanBenar = False
    falseTebakan = 0
    maxTebakan = 3

    while not tebakanBenar :
        while falseTebakan < maxTebakan :
            tebakan = int(input("berapakah aku? : "))

            if tebakan < angkaAcak :
                falseTebakan += 1
                print(f"tebakan kamu masih terlalu kecil!, tersisa {maxTebakan - falseTebakan} kesempatan ")
            elif tebakan > angkaAcak :
                falseTebakan += 1
                print(f"tebakan kamu terlalu besar!, tersisa, {maxTebakan - falseTebakan} percobaan tersisa")
            elif tebakan == angkaAcak :
                print("selamat jawaban kamu benar!")
                tebakanBenar = True
                break
            if falseTebakan == maxTebakan :
                for i in range(10) :
                    print("-", end="")
                print("YOU LOSE! GAME OVER", end="")
                for i in range(10) :
                    print("-", end="")
                print("")
                print("")
                penutupan2()
                break

def penutupan2() :
    tryAgain2 = input("apakah kamu ingin bermain lagi? (y/n) : ")
    if tryAgain2 == "y":
        tebakAngka()
    else :
        for i in range(15) :
            print("-", end="")
        print("Game end", end="")
        for i in range(15) :
            print("-", end="")
        print("")
        for i in range(5) :
            print("-", end="")
        print("thank you for your support!", end="")
        for i in range(5) :
            print("-", end="")
        print("")


if choose == 1 :
    for i in range(5) :
        print("-", end="")
    print("kalkulator sederhana", end="")
    for i in range(5) :
        print("-", end="")
    print("")
    kalkulatorSederhana()
    lastChoice()

        
if choose == 2 :
    for i in range(5) :
        print("-", end="")
    print("game tebak angka", end="")
    for i in range(5) :
        print("-", end="")
    print("")
    tebakAngka()
    penutupan2()
