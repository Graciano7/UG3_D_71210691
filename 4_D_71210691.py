input("Masukkan nama lengkap anda : ")
input("Masukkan prodi anda : ")
nilai=input("Masukkan Nilai (dalam huruf) yang anda dapat : ")

try : 
    if nilai == "A":
        print("Nilai Anda adalah 4.0, tbl tbl serem bgt loh")
    elif nilai == "A-" :
        print("Nilai Anda 3.75, kamu keren!")
    elif nilai == "B+" :
        print("Nilai Anda 3.25, kamu keren!")
    elif nilai == "B" :
        print("Nilai Anda 3.0, Keren")
    elif nilai == "B-" :
        print("Nilai Anda 2.75, Kurang semangat belajar nih")
    elif nilai == "C+" :
        print("Nilai Anda 2.25, semangat")
    elif nilai == "C" :
        print("Nilai Anda 2.0, semangat ")
    elif nilai == "D" :
        print("Nilai Anda 1.0, apakah sudah ada pikiran untuk pindah jurusan?")
    elif nilai == "E" :
        print("Nilai Anda 0, Niat kuliah gak sih?!")
    elif nilai == "F" :
        print("Inputan nilai yang anda masukkan tidak valid")
except:
    print(nilai)
