saldo = int(input("Masukkan saldo anda: "))
lanjut_beli = "y"

def beli_pulsa(p):
    global saldo
    if saldo >= int(p):
        saldo -= int(p)
        print("anda berhasil membeli pulsa Rp.",p)
        print("sisa saldo anda adalah Rp.",saldo)
    else:
        print("Ops saldo anda tidak cukup")
 
 
while lanjut_beli == "y" :
    print("Nayla Dwi Septiana Cellular")
    print("Jl. Gajahmada Tegal No.1")
    print("---------------------------")
    print("1.Beli pulsa Rp.5.000")
    print("2.Beli Pulsa Rp.10.000")
    print("3.Beli Pulsa Rp.20.000")
    print("4.Beli Pulsa Kostum")
    print("5.Keluar aplikasi")
    print("Terimakasih")
    a = int(input("Silahkan pilih pulsa yang mau di beli : "))
    if a == 1:
        beli_pulsa(5000)
    elif a == 2:
        beli_pulsa(10000)
    elif a == 3:
        beli_pulsa(5000)
    elif a == 4:
        beli_pulsa(input("Silahkan masukan nominal pulsa yang akan diisi Rp."))
    elif a == 5:
        lanjut_beli = "n"
    else:
        print("pilihan tidak tersedia")
    lanjut_beli = input("Mau isi pulsa lagi?(y/n)")
