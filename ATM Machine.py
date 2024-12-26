import time
nominal = 5000000
def display_depan():
    pesan = "Selamat Datang Di Bank GoodPeople"
    kotak = len(pesan)
    print("=" * kotak)
    print(pesan)
    print("=" * kotak)

def menu_pilihan():
    print(" " * 8 + "PILIH TRANSAKSI")
    print(" " * 6 + "YANG ANDA INGINKAN")
    print(" " * 2 + "TEKAN CANCEL UNTUK PEMBATALAN")
    print()
    for item in menu:
        print("<" + "--" + item)
    print()

def transfer():
    global nominal
    false_pin = False
    pin_correct = "002004"
    waitTime, wait_Transfer = 24, 3
    false_attempts, correct_attempts = 0, 3
    rekeningTujuan= 0

    while not false_pin:
        while pin_correct != false_pin:
            print("=" * 26)
            pin_input = input("masukkan pin anda : ")
            print("=" * 26)
            if pin_input == pin_correct:
                false_pin = True
                print()
                nominal_input = float(input("masukkan nominal transfer : "))
                rekeningTujuan = int(input("Rekening Tujuan : "))
                print("sedang diproses..\n")
                time.sleep(wait_Transfer)

                if nominal > nominal_input:
                    nominal -= nominal_input
                    print("-" * 45)
                    print(f"Transfer berhasil, sisa saldo kamu Rp{nominal}.")
                    print("-" * 45)
                    break
                    transaksi_selesai()
                else:
                    print("saldo tidak mencukupi")
                    break
            else:
                false_attempts += 1
                print("pin salah !")

            if false_attempts == correct_attempts:
                print("pin salah!, akun anda terblokir 24 jam, konfirmasi ke pihak bank untuk membuka rekening anda.")
                time.sleep(waitTime)
                print("masukkan pin anda : ")
                false_attempts = 0

def transaksi_selesai():
    print("-" * 45)
    print(" " * 10 + "TRANSAKSI TELAH SELESAI")
    print(" " * 15 + "TERIMA KASIH!")
    print("-" * 45)

def transaksi_selanjutnya():
    print()
    print("-" * 45)
    print()
    transaksi_lagi = input("PERLU TRANSAKSI LAGI? (Y/N) : ")
    print("-" * 45)

    wait_Transfer = 3
    if transaksi_lagi in ["Y", "y"]:
        print("\nmemulai transaksi baru..\n")
        time.sleep(wait_Transfer)
        display_depan()
        menu_pilihan()
        menu_utama()
        transaksi_selesai()
        transaksi_selanjutnya()
    elif transaksi_lagi in ["N", "n"]:
        transaksi_selesai()
        exit()

def tampilan_garis_choose2():
    lebar = 30
    print("-" * lebar)
    print("SILAHKAN PILIH".center(lebar))
    print("JENIS PEMBAYARAN/PEMBELIAN".center(lebar))
    print("TEKAN CANCEL UNTUK PEMBATALAN".center(lebar))
    print("-" * lebar)
    for item in menu_transaksi:
        print("<" + "--" + item)

def pin_ATM():
    attempts = 3
    true_pin = False
    wrong_attempts = 0
    pinAtm = "002004"
    while not true_pin:
        print("\n" + "-" * 26)
        pin_atm = input("masukkan pin anda : ")
        print("-" * 26)
        if pin_atm == pinAtm:
            print("sedang diproses.."); time.sleep(2)
            true_pin = True
            print()
            break
        else:
            print("pin salah")
            wrong_attempts += 1
        if wrong_attempts == attempts:
            print("akun anda terblokir, konfirmasi ke pihak bank untuk membuka rekening anda.")
            time.sleep(15)
            break

def PLN_LISTRIK():
    global nominal
    print("-" * 30)
    print(" " * 11 + "MASUKKAN")
    print(" " * 4 + "NOMOR PELANGGAN ANDA")
    print(" " * 7 + "( 5 - 6 DIGIT )")
    print("-" * 30)

    for i in range (11) :
        print(" ", end="")
    no_pelanggan = int(input())
    print(" " * 11 + "-" * 6)

    if len(str(no_pelanggan)) in [5, 6]:
        print("\nsedang diproses..")
        time.sleep(2)
        print()
        print("-" * 30)

        input_transfer = int(input("masukkan nominal transfer\nRp."))

        print("-" * 30)
        if input_transfer < nominal:
            nominal -= input_transfer
            print("\nsedang diproses..")
            time.sleep(3)
            print(f"pembayaran berhasil, sisa saldo kamu Rp{nominal}")
        elif input_transfer > nominal:
            time.sleep(3)
            print("saldo tidak mencukupi")
            return pin_ATM()
        else:
            print("input tidak valid")

def pilihan_operator():
    global nominal
    operator = ["TELKOMSEL (1)", "INDOSAT (2)", "XL (3)", "AXIS (4)", "THREE (5)", "KEMBALI (6)"] 
    for item in operator:
        print("<" + "--" + item)
    input_operator = int(input("Input operator (1-6) : " + "\n"))

    print("-" * 25)
    print("MASUKKAN NO TELEPON ANDA")
    input_noHp = int(" " * 3 + input().center(25))
    print("-" * 25)

    print()
    nominal_pulsa = int(input("masukkan nominal pulsa : Rp. "))
    print()
    if nominal_pulsa > nominal:
        time.sleep(2)
        print("saldo tidak mencukupi")
        display_depan()
        menu_pilihan()
        menu_utama()
    elif nominal_pulsa < nominal:
        nominal -= nominal_pulsa
        time.sleep(2)
        print(f"pembelian pulsa berhasil, sisa saldo kamu Rp{nominal}")
    elif input_operator == 6:
        cancel()

def Telepon () :
    global nominal
    print()
    pilihan_telepon = ["TELPON RUMAH (1)", "TELPON KANTOR (2)", "KEMBALI (3)"]
    for menu in pilihan_telepon :
        print ("<" + "--" + menu)
    print()
    pilihan_user = int(input("masukkan pilihan anda (1-3) : "))

    if pilihan_user == 1 :
        print ("-" * 25)
        print ("MASUKKAN NOMOR TELEPON RUMAH ANDA".center(25))
        print (" " * 9, end = "")
        input_nomor = str(input(""))
        print (" " * 9 + "-" * len(input_nomor))
        transfer_telepon = int(input("masukkan nominal pulsa : Rp. "))
        if transfer_telepon > nominal :
            time.sleep(2)
            print("saldo tidak mencukupi")
            display_depan()
            menu_pilihan()
            menu_utama()
        elif transfer_telepon < nominal :
            nominal -= transfer_telepon
            time.sleep(2)
            print(f"pembelian pulsa berhasil, sisa saldo kamu Rp{nominal}")
            transaksi_selesai()
            transaksi_selanjutnya()
    elif pilihan_user == 2 :
        print ("-" * 25)
        print ("MASUKKAN NOMOR TELEPON INSTANSI".center(25))
        print (" " * 8, end = "")
        input_nomor = str(input(""))
        print (" " * 8 + "-" * len(input_nomor))
        transfer_telepon = int(input("masukkan nominal pulsa : Rp. "))
        if transfer_telepon > nominal :
            time.sleep(2)
            print("saldo tidak mencukupi")
            display_depan()
            menu_pilihan()
            menu_utama()
        elif transfer_telepon < nominal :
            nominal -= transfer_telepon
            print("sedang diproses..")
            time.sleep(2)
            print(f"pembelian pulsa berhasil, sisa saldo kamu Rp{nominal}")
            transaksi_selesai()
            transaksi_selanjutnya()
    elif pilihan_user == 3 :
        cancel()

def penarikan_tunai() :
    global nominal
    nominal_tarik = 0
    tarik_tunai = ["100.000 (1)","200.000 (2)", "300.000 (3)", "500.000 (4)", "JUMLAH LAIN (5)", "KEMBALI (6)"]
    for item in tarik_tunai :
        print("<" + "--" + item)
        print()
    pilihan_tarikTunai = int(input("masukkan pilihan anda (1-6) : "))
    if pilihan_tarikTunai == 1 :
        nominal_tarik = 100000
        print("sedang diproses..")
        time.sleep(2)
    elif pilihan_tarikTunai == 2 :
        nominal_tarik = 200000
        print("sedang diproses..")
        time.sleep(2)
    elif pilihan_tarikTunai == 3 :
        nominal_tarik = 300000
        print("sedang diproses..")
        time.sleep(2)
    elif pilihan_tarikTunai == 4 :
        nominal_tarik = 500000
        print("sedang diproses..")
        time.sleep(2)
    elif pilihan_tarikTunai == 5 :
        nominal_input = int(input("masukkan nominal penarikan : Rp. "))
        print("sedang diproses...")
        time.sleep(2)
    elif pilihan_tarikTunai == 6 :
        cancel()

    if nominal_tarik > nominal :
        time.sleep(2)
        print("saldo tidak mencukupi")
        display_depan()
        menu_pilihan()
        menu_utama()
    elif nominal_tarik < nominal :
        nominal -= nominal_tarik
        time.sleep(2)
        print()
        print(f"penarikan tunai berhasil, sisa saldo kamu Rp.{nominal}")
        print()
    else :
        print("input tidak valid")
        return penarikan_tunai()
    
def informasi_saldo():
    global nominal
    time.sleep(2)
    print()
    print("saldo anda saat ini Rp." + str(nominal))
    print()
    transaksi_selanjutnya()
    
def menu_utama():
    pilihan = input("Input menu (1-5) : ")
    if pilihan == "1":
        transfer()
        transaksi_selesai()
        transaksi_selanjutnya()
    elif pilihan == "2":
        tampilan_garis_choose2()
        pilihan_menuUtama2()
        pin_ATM()
        PLN_LISTRIK()
        transaksi_selesai()
        transaksi_selanjutnya()
    elif pilihan == "3":
        pin_ATM()
        penarikan_tunai()
    elif pilihan == "4":
        informasi_saldo()
    elif pilihan == "5":
        cancel()

def pilihan_menuUtama2():
    pilihan = input("\nInput menu (1-4) : ")
    if pilihan == "1":
        pin_ATM()
        PLN_LISTRIK()
        transaksi_selesai()
        transaksi_selanjutnya()
    elif pilihan == "2":
        pin_ATM()
        pilihan_operator()
        transaksi_selesai()
        transaksi_selanjutnya()
    elif pilihan == "3":
        pin_ATM()
        Telepon()  
    elif pilihan == "4" :
        cancel()

def cancel () :
    display_depan()
    menu_pilihan()
    menu_utama()


#SISTEM OPERASI MULAI DARI SINI
menu = ["Transfer (1)", "Pembayaran/Pembelian (2)", "Penarikan Tunai (3)", "Informasi saldo (4)", "Cancel (5)"]
menu_transaksi = ["PLN/LISTRIK (1)", "PULSA (2)", "TELEPON (3)", "KEMBALI (4)"]

display_depan()
menu_pilihan()
choose = input("Input menu (1-5) : ")
if choose == "1":
    transfer()
    transaksi_selesai()
    transaksi_selanjutnya()
elif choose == "2":
    tampilan_garis_choose2()
    pilihan_menuUtama2()
    pin_ATM()
    PLN_LISTRIK()
    transaksi_selesai()
    transaksi_selanjutnya()
elif choose == "3":
    pin_ATM()
    penarikan_tunai()
    transaksi_selesai()
    transaksi_selanjutnya()
elif choose == "4":
    informasi_saldo()
    transaksi_selanjutnya()
elif choose == "5":
    cancel()
    exit()


