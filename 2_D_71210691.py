plat = float(input("Masukkan Plat Nomor : "))

try: 
    plat=float(plat)
    if  plat >= 5001:
        print("Plat nomor tidak terindikasi ketiga angkutan tersebut")
    elif plat >= 4001:
        print("Plat Nomor tersebut diperuntukan untuk angkutan umum")
    elif plat >= 3001:
        print("Plat nomor tersebut diperuntukan untuk motor")
    elif plat >= 0:
        print("Plat nomor tersebut diperuntukan untuk mobil")
except:

    print(plat)